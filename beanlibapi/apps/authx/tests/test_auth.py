import pytest

from django.contrib.auth import get_user_model
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestUsers:
    @classmethod
    def setup_class(cls):
        cls.client = APIClient()

    def test_signup_should_create_user2(self):
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
        assert user.email == 'testuser2@test2.com'
        assert user.username == 'testuser2'

    def test_signin_with_valid_user_should_return_200_ok(self, user1):
        response = self.client.post(
            '/auth/signin/',
            {
                'email': 'user1@gmail.com',
                'password': 'mysecretpassword1',
            }
        )
        assert response.status_code == 200
