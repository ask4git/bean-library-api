# -*- coding: utf-8 -*-

from django.contrib.auth.models import UserManager as _UserManager
from django.db import (
    models
)

from django.apps import apps


# class UserManager(_UserManager):
#     pass


# class BeanManager(models.Manager):
#     def create_bean(self, validated_data):
#         print(validated_data)
#         obj = self.create(name=validated_data.get('name'))
#         bean_detail = apps.get_model('core', 'BeanDetail')
#         validated_data.update({"bean": obj})
#         bean_detail.objects.create(validated_data)
#         return obj
