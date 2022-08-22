from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
    def _create_user(self, user_name, email, last_name, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            user_name = user_name,
            email=self.normalize_email(email),
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, user_name,last_name, password=None, **extra_fields):
        return self._create_user(email, user_name,last_name, password, False, False, **extra_fields)

    def create_superuser(self, user_name, email, last_name, password=None, **extra_fields):
        return self._create_user(user_name, email, last_name, password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    user_name = models.CharField(max_length = 255, unique = True)
    email = models.EmailField('Correo Electrónico',max_length = 255, unique = True,)
    last_name = models.CharField('Apellidos', max_length = 255, blank = True, null = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['email','last_name']

    def __str__(self):
        return f'{self.user_name} {self.last_name}'