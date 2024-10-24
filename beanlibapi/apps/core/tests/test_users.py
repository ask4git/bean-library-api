import pytest
from django.contrib.auth import get_user_model
from rest_framework import status
from beanlibapi.apps.core import models as m
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestUsers:
    @classmethod
    def setup_class(cls):
        cls.client = APIClient()
        cls.data = {
            'username': 'testuser',
            'email': 'testuser@test.com',
            'password1': 'mytopsecret1',
            'password2': 'mytopsecret1'
        }

    def test_signup_should_create_user1(self):
        response = self.client.post(
            '/dj-rest-auth/registration/',
            self.data
        )
        assert response.status_code == 201
        user_model = get_user_model()
        user = user_model.objects.get(username=self.data.get('username'))
        assert user.email == self.data.get('email')
        assert user.username == self.data.get('username')

    def test_signup_should_create_user2(self):
        response = self.client.post(
            '/auth/sign-up/',
            self.data
        )
        assert response.status_code == 201
        user_model = get_user_model()
        user = user_model.objects.get(username=self.data.get('username'))
        assert user.email == self.data.get('email')
        assert user.username == self.data.get('username')

    def test_signin_should_return_200ok(self, user2):
        response = self.client.post(
            '/auth/sign-in/',
            {
                'username': 'user2',
                'password': 'mypassword',
            }
        )
        assert response.status_code == 200
