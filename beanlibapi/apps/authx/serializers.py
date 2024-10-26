from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm

from dj_rest_auth.registration.serializers import (
    RegisterSerializer as _RegisterSerializer,
)
from dj_rest_auth.serializers import (
    PasswordResetSerializer as _PasswordResetSerializer,
)

if 'allauth' in settings.INSTALLED_APPS:
    from .forms import AllAuthPasswordResetForm


class RegisterSerializer(_RegisterSerializer):
    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data.update({'first_name': self.validated_data.get('first_name', '')})
        data.update({'last_name': self.validated_data.get('last_name', '')})
        data.update({'phone_number': self.validated_data.get('phone_number', '')})
        return data


class PasswordResetSerializer(_PasswordResetSerializer):
    @property
    def password_reset_form_class(self):
        if 'allauth' in settings.INSTALLED_APPS:
            return AllAuthPasswordResetForm
        else:
            return PasswordResetForm
