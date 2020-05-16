from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

#SOURCE: https://www.youtube.com/watch?v=tUqUdu0Sjyc

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # fields = ['username', 'password1', 'password2']
