from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from .managers import UserManager


# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True, max_length=300)
    email_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_admin