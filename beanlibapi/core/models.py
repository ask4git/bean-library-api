import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from beanlibapi.core import (
    model_managers as mm,
    model_mixins as mx,
    constants as c,
)
from enumfields import EnumField


class Bean(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True, unique=True, editable=False)
    name = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    variety = models.CharField(max_length=255)
    process = models.CharField(max_length=255)
    producer = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    is_active = models.BooleanField(default=True)

    # objects = mm.BeanManager()

    class Meta:
        ordering = ['created_at']


class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_deleted = models.BooleanField(default=False)
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(db_index=True, auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(db_index=True, auto_now=True)


# class BeanProduct

# class BeanDetail(models.Model):
#     uid = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True, unique=True, editable=False)
#     bean = models.OneToOneField('Bean', on_delete=models.CASCADE, db_column='bean_uid')
#     name = models.CharField(max_length=255)
#     process = EnumField(c.BeanProcess, max_length=50, default=c.BeanProcess.Unknown)
#     region = EnumField(c.BeanRegion, max_length=50, default=c.BeanRegion.Unknown)
#     producer = models.CharField(max_length=255)
#     # location
#     variety = models.CharField(max_length=255)
#     # flavour


class User(AbstractUser, mx.UserMixin):
    deleted = models.BooleanField(db_index=True, null=True, blank=True)
    deleted_at = models.DateTimeField(db_index=True, null=True, blank=True)

    # objects = mm.UserManager()
