from django import forms
from .models import Driver
from .models import HireRequest, Message

class HireRequestForm(forms.ModelForm):
    class Meta:
        model = HireRequest
        fields = ['ambulance', 'current_location', 'destination']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['phone', 'profile_pic']
