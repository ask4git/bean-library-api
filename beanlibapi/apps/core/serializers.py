from django.contrib.auth import get_user_model
from rest_framework import serializers as s

from dj_rest_auth.registration.serializers import (
    RegisterSerializer as _RegisterSerializer,
)
from dj_rest_auth.serializers import (
    LoginSerializer as _LoginSerializer,
)
from beanlibapi.apps.core.models import Bean, Attachment, Cafe

user_model = get_user_model()


class CustomRegisterSerializer(_RegisterSerializer):
    first_name = s.CharField(required=True)
    last_name = s.CharField(required=True)
    phone_number = s.CharField(required=True)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['first_name'] = self.validated_data.get('first_name', '')
        data['last_name'] = self.validated_data.get('last_name', '')
        data['phone_number'] = self.validated_data.get('phone_number', '')
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


class AttachmentSerializer(s.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ['name', 'format']


class CafeWriteSerializer(s.ModelSerializer):
    class Meta:
        model = Cafe
        fields = '__all__'
        extra_kwargs = {
            'owner': {'read_only': True, 'required': False},
        }


class CafeSerializer(s.ModelSerializer):
    image = s.SerializerMethodField()
    title = s.CharField(source='name')
    author = s.CharField(source='uid')

    class Meta:
        model = Cafe
        fields = ['image', 'title', 'author']
        extra_kwargs = {
            'owner': {'read_only': True, 'required': False},
        }

    @staticmethod
    def get_image(obj):
        if isinstance(obj.images, list) and obj.images:
            return obj.images[0]
        return [""]


class CafeDetailSerializer(s.ModelSerializer):
    class Meta:
        model = Cafe
        fields = ['images']
