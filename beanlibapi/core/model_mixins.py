# # -*- coding: utf-8 -*-
#
# from django.db import (
#     models
# )
#
#
# class BeanMixin(models.manager):
#     pass


class UserMixin:
    def __str__(self):
        return self.email

    @property
    def is_authenticated(self):
        return self.is_active


class AttachmentMixin:
    def __str__(self):
        return self.filename