from .manager import EmailUserManager
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(_('Email'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = EmailUserManager()

    phone = models.IntegerField('номер телефона', null=True)
    is_manager = models.BooleanField('является менеджером', default=False)

    def __str__(self):
        return f'{self.get_full_name()} {self.email}'