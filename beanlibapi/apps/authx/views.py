from dj_rest_auth.registration.views import (
    RegisterView as _RegisterView,
    LoginView as _LoginView
)

from beanlibapi.apps.core import serializers as s


class RegisterView(_RegisterView):
    serializer_class = s.RegisterSerializer


class LoginView(_LoginView):
    serializer_class = s.LoginSerializer
