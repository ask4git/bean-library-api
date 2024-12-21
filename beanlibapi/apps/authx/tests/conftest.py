import pytest
from allauth.account.models import EmailAddress
# from django.contrib.sites.models import Site
from django.contrib.auth import get_user_model
from rest_framework.authtoken import models as am


# from allauth.socialaccount.models import SocialApp


@pytest.fixture
def verified_user1():
    user_model = get_user_model()
    user = user_model.objects.create_user(
        username='verified_user1',
        email='verified_user1@gmail.com',
        password='mysecretpassword1'
    )
    EmailAddress.objects.create(
        user=user,
        email=user.email,
        verified=True,
        primary=True
    )
    user.save()


@pytest.fixture
def unverified_user1():
    user_model = get_user_model()
    user = user_model.objects.create_user(
        username='unverified_user1',
        email='unverified_user1@gmail.com',
        password='mysecretpassword1'
    )
    EmailAddress.objects.create(
        user=user,
        email=user.email,
        verified=False,
        primary=False
    )
    user.save()


@pytest.fixture
def user2():
    user_model = get_user_model()
    user = user_model.objects.create_user(
        username='user2',
        email='user2@gmail.com',
        password='mysecretpassword2'
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

#
# @pytest.fixture
# def django_site1():
#     return Site.objects.create(domain='test.com', name='test')
#
#
# @pytest.fixture
# def social_app_google1():
#     return SocialApp.objects.create(
#         provider='google',
#         provider_id='google_1234567890',
#         client_id='1234567890',
#         secret='abcdefg',
#         name='google',
#     )
