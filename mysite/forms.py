# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Usuario
        fields = ('username', 'email')

class LatLngForm(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = ('latitude','longitude')