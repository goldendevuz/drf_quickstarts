from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone_numbers = models.JSONField(default=list)
    skills = models.JSONField(default=list)
    bookmarks = models.JSONField(default=dict)
    measurements = models.JSONField(default=dict) # Stores height and weight as measurements

    def __str__(self):
        return self.username
