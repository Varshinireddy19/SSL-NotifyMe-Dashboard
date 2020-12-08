from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate





class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    roles = [
        ('user', 'Student'),
        ('admin', 'Professor'),
        ('user', 'TA')
    ]
    role = forms.ChoiceField(choices=roles, widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']

