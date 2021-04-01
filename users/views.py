from django.shortcuts import render, redirect
from django.contrib import (
    messages,
)  # the messages contrib has a library of different html messages that can be used, such as one-time flash
from .forms import (
    UserRegisterForm,
)  # We are importing our own form, which is based on the UserCreationForm provided by Django


def register(request):
    # The method on this form is POST. When the submit button refreshes the page, the method of the request will therefore be POST.
    # This conditional logic loks for the POST method, and presents a success message from the messages library imported above
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # This automatically hashes the password and saves the data to the user data
            username = form.cleaned_data.get(
                "username"
            )  # django forms have a cleaned-data dictionary where values from the form can be retrieved
            messages.success(request, f"Account created for{username}!")
            return redirect(
                "blog-home"
            )  # Here we use the redirect function, imported above, and pass in the url pattern name from blog/urls.py
    else:
        form = UserRegisterForm()

    return render(
        request, "users/register.html", {"form": form}
    )  # Note how we're passing in the form object as the context argument for the render function. This means it can be used in the register.html template
