import pytest
from rest_framework import status
from beanlibapi.apps.core import models as m
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestBean:
    # @pytest.fixture(autouse=True)
    @classmethod
    def setup_class(cls):
        cls.client = APIClient()
        cls.data = {
            "name": "Colombia Granja La Esperanza Cerro Azul Geisha Honey",
            "region": "colombia",
            "variety": "geisha",
            "process": "natural"
        }

    def setup_method(self):
        self.client.force_authenticate(user=None)

    def test_query_should_not_return_inactive_data(self, bean1, bean2, bean1_inactive):
        assert m.Bean.objects.all().count() == 2

    def test_should_not_return_inactive_bean_via_get(self, bean1, bean2, bean1_inactive):
        response = self.client.get('/core/bean/')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2

    def test_authenticated_user_can_create_bean_via_post(self, superuser, bean1, bean2, bean1_inactive):
        self.client.force_authenticate(user=superuser)
        self.num_of_beans = 2

        response = self.client.get('/core/bean/')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == self.num_of_beans

        response = self.client.post('/core/bean/', data=self.data, format='json')
        assert response.status_code == status.HTTP_201_CREATED

        response = self.client.get('/core/bean/')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == self.num_of_beans + 1

    def test_user_cannot_create_bean_via_post(self, user1, bean1, bean2, bean1_inactive):
        self.client.force_authenticate(user=user1)
        self.num_of_beans = 2

        response = self.client.get('/core/bean/')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == self.num_of_beans

        response = self.client.post('/core/bean/', data=self.data, format='json')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

        response = self.client.get('/core/bean/')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == self.num_of_beans
