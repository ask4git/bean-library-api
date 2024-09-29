from rest_framework import permissions as p
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from dj_rest_auth.registration.views import (
    RegisterView as _RegisterView,
    LoginView as _LoginView
)

from beanlibapi.core import (
    models as m,
    serializers as s,
)


# from beanlibapi.core.permissions import IsOwnerOrReadOnly


class RegisterView(_RegisterView):
    serializer_class = s.RegisterSerializer


class LoginView(_LoginView):
    serializer_class = s.LoginSerializer


class BeanListCreateView(ListCreateAPIView):
    queryset = m.Bean.objects
    serializer_class = s.BeanSerializer
    permission_classes = [p.IsAuthenticatedOrReadOnly]


class BeanRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = m.Bean.objects
    serializer_class = s.BeanSerializer
    # permission_classes = [p.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    permission_classes = [p.IsAuthenticatedOrReadOnly]
