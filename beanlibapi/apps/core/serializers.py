from django.contrib.auth import get_user_model
from rest_framework import serializers as s

from dj_rest_auth.registration.serializers import (
    RegisterSerializer as _RegisterSerializer,
)
from dj_rest_auth.serializers import (
    LoginSerializer as _LoginSerializer,
)
from beanlibapi.apps.core.models import Bean

user_model = get_user_model()


class CustomRegisterSerializer(_RegisterSerializer):
    first_name = s.CharField(required=True)
    last_name = s.CharField(required=True)
    phone_number = s.CharField(required=True)  # 커스텀 필드 추가

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['first_name'] = self.validated_data.get('first_name', '')
        data['last_name'] = self.validated_data.get('last_name', '')
        data['phone_number'] = self.validated_data.get('phone_number', '')  # 커스텀 필드
        return data


class BeanSerializer(s.ModelSerializer):
    class Meta:
        model = Bean
        fields = ['uid', 'name', 'region', 'variety', 'process', 'is_active', ]


class UserSerializer(s.ModelSerializer):
    class Meta:
        model = user_model
        fields = ('id', 'username', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = user_model.objects.create_user(**validated_data)
        return user


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
