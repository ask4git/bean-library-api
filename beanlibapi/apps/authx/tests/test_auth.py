import pytest
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient
from allauth.account.models import EmailAddress
from beanlibapi.apps.core.utils.test import get_json_response


@pytest.mark.django_db
class TestUsers:
    @classmethod
    def setup_class(cls):
        cls.client = APIClient()

    def test_signup_should_create_unverified_user(self):
        response = self.client.post(
            '/auth/signup/',
            {
                'username': 'testuser2',
                'email': 'testuser2@test2.com',
                'password1': 'mytopsecret1',
                'password2': 'mytopsecret1'
            }
        )
        assert response.status_code == 201
        user_model = get_user_model()
        user = user_model.objects.get(username='testuser2')
        email_address = EmailAddress.objects.get(user=user)
        assert user.email == 'testuser2@test2.com'
        assert user.username == 'testuser2'
        assert email_address.verified == False

    def test_signin_with_verified_user_should_return_200_ok(self, verified_user1):
        response = self.client.post(
            '/auth/signin/',
            {
                'email': 'verified_user1@gmail.com',
                'password': 'mysecretpassword1',
            }
        )
        assert response.status_code == status.HTTP_200_OK

    def test_signin_with_unverified_user_should_return_400_bad_request(self, unverified_user1):
        response = self.client.post(
            '/auth/signin/',
            {
                'email': 'unverified_user1@gmail.com',
                'password': 'mysecretpassword1',
            }
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        json_response = get_json_response(response)
        error_message = json_response['non_field_errors'][0]
        assert error_message == 'E-mail is not verified.'

    # def test_signup_with_google_should_return_redirect_url(self):
    #     response = self.client.get(
    #         '/auth/api/social-login/google/'
    #     )
    #     print(response.data)
    #     assert response.status_code == status.HTTP_200_OK
