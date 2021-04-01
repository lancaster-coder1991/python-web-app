from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm # We can import premade HTML forms from djangos contrib library

def register():
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form}}) # Note how we're passing in the form object as the context argument for the render function. This means it can be used in the register.html template