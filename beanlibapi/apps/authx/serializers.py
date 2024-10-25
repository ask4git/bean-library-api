from dj_rest_auth.registration.serializers import (
    RegisterSerializer as _RegisterSerializer,
)
from dj_rest_auth.serializers import (
    LoginSerializer as _LoginSerializer,
)


class RegisterSerializer(_RegisterSerializer):
    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['first_name'] = self.validated_data.get('first_name', '')
        data['last_name'] = self.validated_data.get('last_name', '')
        data['phone_number'] = self.validated_data.get('phone_number', '')  # 커스텀 필드
        return data


class LoginSerializer(_LoginSerializer):
    def get_cleaned_data(self):
        print(self.validated_data)
