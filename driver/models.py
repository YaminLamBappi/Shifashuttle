from django.db import models
from phone_field import PhoneField
from django.conf import settings
from user_account.models import CustomUser

class Ambulance(models.Model):
    registration_number = models.CharField(max_length=50, unique=True)
    model = models.CharField(max_length=100)
    capacity = models.IntegerField()
    status_choices = [
        ('available', 'Available'),
        ('on_call', 'On Call'),
        ('in_service', 'In Service'),
    ]
    status = models.CharField(max_length=20, choices=status_choices)
    location = models.CharField(max_length=255)  # Field for entering location by text

    def __str__(self):
        return self.registration_number


class Driver(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    ambulances = models.ManyToManyField(Ambulance, blank=True)
    phone = PhoneField(blank=True, null=True, help_text='Contact phone number')
    profile_pic = models.ImageField(upload_to='driver_profile_pics/', default='default.png')



    def __str__(self):
        return self.user.username
