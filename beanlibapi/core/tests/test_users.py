import pytest
from rest_framework import status

from rest_framework.test import APIClient


@pytest.mark.django_db
def test_user_list(client: APIClient):
    response = client.post('/bean/')
    assert response.status_code == status.HTTP_200_OK
