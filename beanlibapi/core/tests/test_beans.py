import pytest
from rest_framework import status
from beanlibapi.core import (
    models as m
)

from rest_framework.test import APIClient


@pytest.mark.django_db
def test_bean_list(bean1, bean2, bean3_inactive):
    cnt = m.Bean.objects.all().count()
    assert cnt == 3


@pytest.mark.django_db
def test_bean_list2():
    flag = False
    assert flag is False


@pytest.mark.django_db
def test_bean_list3():
    flag = True
    assert flag is True


@pytest.mark.django_db
def test_bean_get(bean1, bean2, bean3_inactive):
    client = APIClient()
    response = client.get('/bean/')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2


@pytest.mark.django_db
def test_superuser_can_create_bean_via_post(superuser, bean1, bean2, bean3_inactive):
    client = APIClient()
    client.force_authenticate(user=superuser)

    response = client.get('/bean/')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2

    data = {
        "name": "Colombia Granja La Esperanza Cerro Azul Geisha Honey",
        "region": "colombia",
        "variety": "geisha",
        "process": "natural"
    }
    response = client.post('/bean/', data=data, format='json')
    print(response.data)
    assert response.status_code == status.HTTP_201_CREATED
    response = client.get('/bean/')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 3


@pytest.mark.django_db
def test_user_cannot_create_bean_via_post(user2, bean1, bean2, bean3_inactive):
    client = APIClient()
    client.force_authenticate(user=user2)

    response = client.get('/bean/')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2

    data = {
        "name": "Colombia Granja La Esperanza Cerro Azul Geisha Honey",
        "region": "colombia",
        "variety": "geisha",
        "process": "natural"
    }
    response = client.post('/bean/', data=data, format='json')
    print(response.data)
    assert response.status_code == status.HTTP_403_FORBIDDEN
    response = client.get('/bean/')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2
