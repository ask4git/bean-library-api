from rest_framework import serializers as s
from beanlibapi.core.models import Bean, User
from django.apps import apps
# from rest_auth.registration.serializers import RegisterSerializer as _RegisterSerializer

# class BeanSerializer(s.Serializer):
#     uid = s.CharField(read_only=True)
#     name = s.CharField(read_only=False, allow_blank=True, max_length=255)
#     created_at = s.DateTimeField(read_only=True)
#
#     def create(self, validated_data):
#         return Bean.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.save()
#         return instance
class BeanSerializer(s.ModelSerializer):
    # def create(self, validated_data):
    #     # bean = apps.get_model('core', 'Bean')
    #     # return bean.objects.create_bean(validated_data)
    #     return Bean.objects.create_bean(validated_data)

    class Meta:
        model = Bean
        fields = ['uid', 'name', 'region', 'variety', 'process', 'is_active', ]


class UserSerializer(s.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


# class RegisterSerializer(_RegisterSerializer):
#     first_name = s.CharField(required=False)
#     last_name = s.CharField(required=False)