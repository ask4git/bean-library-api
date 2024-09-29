from rest_framework import permissions as p
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,

)
from dj_rest_auth.registration.views import (
    RegisterView as _RegisterView,
)

from beanlibapi.core.models import Bean
from beanlibapi.core.serializers import (
    BeanSerializer,
    UserRegisterSerializer,
)
from beanlibapi.core.permissions import IsOwnerOrReadOnly


class UserRegisterView(_RegisterView):
    serializer_class = UserRegisterSerializer


class BeanListCreateView(ListCreateAPIView):
    queryset = Bean.objects.all()
    serializer_class = BeanSerializer
    permission_classes = [p.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Bean.objects.filter(is_active=True)


class BeanRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Bean.objects.all()
    serializer_class = BeanSerializer
    # permission_classes = [p.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    permission_classes = [p.IsAuthenticatedOrReadOnly]
