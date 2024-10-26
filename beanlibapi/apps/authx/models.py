from django.db import models
from django.contrib.auth.models import AbstractUser


from beanlibapi.apps.authx import model_managers as mm


class User(AbstractUser):
    deleted = models.BooleanField(db_index=True, null=True, blank=True)
    deleted_at = models.DateTimeField(db_index=True, null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    objects = mm.UserManager()

    def __str__(self):
        return self.username
