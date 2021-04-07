from django.shortcuts import render, redirect
from django.contrib import (
    messages,
)  # the messages contrib has a library of different html messages that can be used, such as one-time flash
from .forms import (
    UserRegisterForm,
    UserUpdateForm,
    ProfileUpdateForm,
)  # We are importing our own form, which is based on the UserCreationForm provided by Django
from django.contrib.auth.decorators import (
    login_required,
)  # the decorators property of the auth dictionary provides a decorator which provides functionality to prevent certain pages from being viewed unless the user is logged in


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
            messages.success(
                request,
                f"Your account has been created! You are now about to log in :)",
            )
            return redirect(
                "login"
            )  # Here we use the redirect function, imported above, and pass in the url pattern name
    else:
        form = UserRegisterForm()

    return render(
        request, "users/register.html", {"form": form}
    )  # Note how we're passing in the form object as the context argument for the render function. This means it can be used in the register.html template


@login_required  # This decorator, imported above, means that this page can only be viewed when the user is logged in
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(
            request.POST, instance=request.user
        )  # Passing in this instance argument means that these two forms will be prepopulated with the current user's details, which are accessed via the request parameter of the parent function
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
                request,
                f"Your account has been updated :)",
            )
            return redirect("profile")
    else:
        u_form = UserUpdateForm(
            instance=request.user
        )  # Passing in this instance argument means that these two forms will be prepopulated with the current user's details, which are accessed via the request parameter of the parent function
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "u_form": u_form,
        "p_form": p_form,
    }  # Here we are importing forms from forms.py and adding them to a context dictionary, and then passing this as the third arguments to the render function below so that they can be used in the profile.html template

    return render(request, "users/profile.html", context)
