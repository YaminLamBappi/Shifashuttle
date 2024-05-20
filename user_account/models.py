from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = PhoneField(blank=True, null=True, help_text='Contact phone number')
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', default='default.png')
