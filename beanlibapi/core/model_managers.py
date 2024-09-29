# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import UserManager as _UserManager


class UserManager(_UserManager):
    pass


class BeanManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
