from django.db import models
from django.contrib.auth.models import AbstractUser


NULLABLE = dict(blank=True, null=True)


class User(AbstractUser):
    username = None
    email = models.EmailField('email', unique=True)
    avatar = models.ImageField('avatar', upload_to='avatars/', **NULLABLE)
    phone = models.CharField('phone number', max_length=255, **NULLABLE)
    country = models.CharField('country', max_length=255, **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class VerificationModel(models.Model):
    code = models.IntegerField()
