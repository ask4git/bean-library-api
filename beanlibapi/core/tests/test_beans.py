import pytest
from rest_framework import status
from beanlibapi.core import models as m
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestBean:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = APIClient()

    def test_bean_list(self, bean1, bean2, bean3_inactive):
        cnt = m.Bean.objects.all().count()
        assert cnt == 3

    def test_bean_list2(self):
        flag = False
        assert flag is False

    def test_bean_list3(self):
        flag = True
        assert flag is True

    def test_bean_get(self, bean1, bean2, bean3_inactive):
        response = self.client.get('/core/bean/')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2

    def test_superuser_can_create_bean_via_post(self, superuser, bean1, bean2, bean3_inactive):
        self.client.force_authenticate(user=superuser)

        response = self.client.get('/core/bean/')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2

        data = {
            "name": "Colombia Granja La Esperanza Cerro Azul Geisha Honey",
            "region": "colombia",
            "variety": "geisha",
            "process": "natural"
        }
        response = self.client.post('/core/bean/', data=data, format='json')
        print(response.data)
        assert response.status_code == status.HTTP_201_CREATED
        response = self.client.get('/core/bean/')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 3

    def test_user_cannot_create_bean_via_post(self, user2, bean1, bean2, bean3_inactive):
        self.client.force_authenticate(user=user2)

        response = self.client.get('/core/bean/')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2

        data = {
            "name": "Colombia Granja La Esperanza Cerro Azul Geisha Honey",
            "region": "colombia",
            "variety": "geisha",
            "process": "natural"
        }
        response = self.client.post('/core/bean/', data=data, format='json')
        print(response.data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        response = self.client.get('/core/bean/')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2
