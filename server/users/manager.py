from typing import Dict
from django.db.models import Model
from django.contrib.auth.models import BaseUserManager


class EmailUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email: str, password: str, **kwargs: Dict) -> Model:

        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(
        self, email: str, password: str = None, **kwargs: Dict
    ) -> Model:

        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)
        return self._create_user(email, password, **kwargs)

    def create_superuser(
        self, email: str, password: str = None, **kwargs: Dict
    ) -> Model:

        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')

        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self._create_user(email, password, **kwargs)
