# models.py
from django.db import models
from phone_field import PhoneField
from django.conf import settings
from user_account.models import CustomUser

class Driver(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = PhoneField(blank=True, null=True, help_text='Contact phone number')
    profile_pic = models.ImageField(upload_to='driver_profile_pics/', default='default.png')

    def __str__(self):
        return self.user.username

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
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True, related_name='ambulances')

    def __str__(self):
        return self.registration_number

class HireRequest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ambulance = models.ForeignKey(Ambulance, on_delete=models.CASCADE)
    current_location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    status_choices = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed'),
        
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Hire request by {self.user.username}'

class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField(default=None)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.sender.username} to {self.receiver.username}'


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name