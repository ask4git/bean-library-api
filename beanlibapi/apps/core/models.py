import uuid
from django.conf import settings
from django.db import models

from beanlibapi.apps.core import model_managers as mm, model_mixins as mx

from shortid import ShortId

SID_GENERATOR = ShortId()


def generate_sid():
    return str(SID_GENERATOR.generate())


class Bean(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True, unique=True, editable=False)
    name = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    variety = models.CharField(max_length=255)
    process = models.CharField(max_length=255)
    producer = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    is_active = models.BooleanField(default=True)

    objects = mm.BeanManager()

    class Meta:
        ordering = ['created_at']


class BeanDetail(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True, unique=True, editable=False)
    bean_uid = models.ForeignKey(Bean, on_delete=models.CASCADE)
    context = models.JSONField(default=dict, blank=True)


class Cafe(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True, unique=True, editable=False)
    name = models.CharField(max_length=255)


class Article(models.Model):
    uid = models.CharField(primary_key=True, max_length=24, unique=True, editable=False, default=generate_sid)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_deleted = models.BooleanField(default=False)
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(db_index=True, auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(db_index=True, auto_now=True)


class Attachment(models.Model, mx.AttachmentMixin):
    uid = models.CharField(primary_key=True, max_length=24, unique=True, editable=False, default=generate_sid)
    filename = models.CharField(max_length=255)
    image = models.FileField()
    # path = models.FilePathField(max_length=255)
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bean = models.ForeignKey('Bean', null=True, blank=True, on_delete=models.CASCADE)
