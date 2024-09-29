import pytest
from rest_framework.test import APIClient
from django.contrib.auth import (
    authenticate,
    get_user_model,
)
from django.apps import apps


@pytest.mark.django_db
def test_registration_should_create_user():
    client = APIClient()
    response = client.post(
        '/dj-rest-auth/registration/',
        {
            'username': 'testuser1',
            'email': 'test@test2.com',
            'password1': 'mytopsecret1',
            'password2': 'mytopsecret1'
        }
    )
    assert response.status_code == 201
    user_model = get_user_model()
    user = user_model.objects.get(username='testuser1')
    assert user.email == 'test@test2.com'
    assert user.username == 'testuser1'


@pytest.mark.django_db
def test_registration_should_create_user2():
    client = APIClient()
    response = client.post(
        '/core/auth/sign-up/',
        {
            'username': 'testuser2',
            'email': 'test@test2.com',
            'password1': 'mytopsecret1',
            'password2': 'mytopsecret1'
        }
    )
    assert response.status_code == 201
    user_model = get_user_model()
    user = user_model.objects.get(username='testuser2')
    assert user.email == 'test@test2.com'
    assert user.username == 'testuser2'
