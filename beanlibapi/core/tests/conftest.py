import pytest
from django.contrib.auth import get_user_model


@pytest.fixture
def user1():
    user_model = get_user_model()
    user = user_model.objects.create_user(username='user1', password='mypassword')
    user.save()


@pytest.fixture
def user2():
    user_model = get_user_model()
    user = user_model.objects.create_user(username='user2', password='mypassword')
    user.save()
