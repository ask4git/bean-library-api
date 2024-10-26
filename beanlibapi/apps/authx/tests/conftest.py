import pytest

from django.contrib.auth import get_user_model
from rest_framework.authtoken import models as am


@pytest.fixture
def user1():
    user_model = get_user_model()
    user = user_model.objects.create_user(
        username='user1',
        password='mypassword1'
    )
    user.save()


@pytest.fixture
def user2():
    user_model = get_user_model()
    user = user_model.objects.create_user(
        username='user2',
        password='mypassword2'
    )
    user.save()


@pytest.fixture
def superuser1():
    user_model = get_user_model()
    user = user_model.objects.create_superuser(
        username='superuser1',
        email='superuser1@gmail.com',
        password='mysecretpassword1'
    )
    am.Token.objects.get_or_create(user=user)
    return user
