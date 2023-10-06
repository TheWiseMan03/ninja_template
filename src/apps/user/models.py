from django.db import models


class User(models.Model):

    username = models.CharField(max_length=50)
    age = models.IntegerField()

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
