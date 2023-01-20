from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Custom_User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Custom_User
        fields = '__all__'
