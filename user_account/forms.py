from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from phone_field import PhoneField

class CustomUserCreationForm(UserCreationForm):
    phone = PhoneField( help_text='Contact phone number')

    class Meta:
        model = CustomUser
        fields = [ 'username', 'email', 'phone', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser  
        fields = [
            'first_name', 'last_name', 'email', 
            'phone', 'bio', 'profile_pic']
