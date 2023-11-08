from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import datetime, timezone


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if username is None:
            raise TypeError("username required to login")

        user = self.model(username=username, **extra_fields)
        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        if username is None:
            raise TypeError("username is required to login")
        if password is None:
            raise TypeError("Password is required to login")
        user = self.create_user(username=username, password=password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)



    def __str__(self):
        return self.username
    
    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []


class Token(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    refresh_token = models.CharField(max_length=200)
    refresh_token_expires_at = models.DateTimeField(default=datetime.now(timezone.utc))
