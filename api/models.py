from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone_numbers = models.JSONField(default=list)  # Stores a list of phone numbers
