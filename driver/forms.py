from django import forms
from .models import Driver, Ambulance
from .models import HireRequest, Message

class AmbulanceForm(forms.ModelForm):
    class Meta:
        model = Ambulance
        fields = ['registration_number', 'model', 'capacity', 'status', 'location']


class HireRequestForm(forms.ModelForm):
    class Meta:
        model = HireRequest
        fields = [ 'current_location', 'destination']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['phone', 'profile_pic']
