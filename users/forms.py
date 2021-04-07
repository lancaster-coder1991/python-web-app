from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    UserCreationForm,
)  # We can import premade HTML forms from djangos contrib library
from .models import Profile


class UserRegisterForm(
    UserCreationForm
):  # In order to add new fields to the default UserCreationForm, we cna create a new class that inherits from the base UserCreationForm provided by Django
    email = forms.EmailField()

    class Meta:  # This class Meta gives a namespace for configuring this specific manifestation of the user form
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserUpdateForm(
    forms.ModelForm
):  # This form inherits from ModelForms, which is a class you can use to link forms to database models
    email = forms.EmailField()

    class Meta:  # This class Meta gives a namespace for configuring this specific manifestation of the user form
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]
