from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.username
