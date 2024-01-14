from django.db import models
from django.contrib.auth.models import AbstractUser

class CUser(AbstractUser):
    profile_image = models.ImageField('profile_images/', default='profile_images/default.png')
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']