import pytest

from beanlibapi.apps.core import models as m

from rest_framework.authtoken import models as am
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


@pytest.fixture
def superuser():
    user_model = get_user_model()
    user = user_model.objects.create_superuser('superuser', 'superuser@deepnatural.ai',
                                               'mysecret')
    user.last_name = 'hero'
    am.Token.objects.get_or_create(user=user)
    return user


@pytest.fixture
def bean1():
    bean = m.Bean.objects.create(
        name="Colombia Granja La Esperanza Cerro Azul Geisha Honey",
        region="colombia",
        variety="geisha",
        process="natural",
        producer="La Esperanza",
    )
    return bean


@pytest.fixture
def bean2():
    bean = m.Bean.objects.create(
        name="Ethiopia Sidama Twakok Selection Natural",
        region="ethiopia",
        variety="heirloom",
        process="natural",
        producer=" - ",
    )
    return bean


@pytest.fixture
def bean1_inactive():
    bean = m.Bean.objects.create(
        name="Ethiopia Guji Uraga Siko Natural",
        region="ethiopia",
        variety="Dega & Kurume",
        process="natural",
        producer="472 coffee producers in SIKO village",
        is_active=False
    )
    return bean
