from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username', 'password1', 'password2', 'name',
            'company_name', 'location', 'mobile_number',
            'address', 'industry_type'
        ]
