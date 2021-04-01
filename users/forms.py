from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    UserCreationForm,
)  # We can import premade HTML forms from djangos contrib library


class UserRegisterForm(
    UserCreationForm
):  # In order to add new fields to the default UserCreationForm, we cna create a new class that inherits from the base UserCreationForm provided by Django
    email = forms.EmailField()

    class Meta:  # This class Meta gives a namespace for configuring this specific manifestation of the user form
        model = User
        fields = ["username", "email", "password1", "password2"]
