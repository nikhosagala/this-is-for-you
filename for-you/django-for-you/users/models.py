from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class TimestampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseModel(TimestampedModel):
    name = models.CharField(max_length=70)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class User(AbstractUser, BaseModel):
    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True)
    username = models.CharField(unique=False, blank=True, max_length=150, null=True)
    REQUIRED_FIELDS = []
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)

    objects = UserManager()

    class Meta:
        db_table = 'users'
