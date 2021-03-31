# The render built-in function takes the request as a first argument, then a file path to templates as its second argument.
# The teampltes are HTML files which will display when a particular view is routed to, if the render function has been invoked correctly.
from django.shortcuts import render

# We can use the HttpResponse function from django.http to create content to send to the client when they hit a particular route
# NB this is only needed when templates aren't being used.
from django.http import HttpResponse


def home(request):
    return render(
        request, "blog/home.html"
    )  # No need to add /templates to the directory here, as Django automatically loks in this folder for templates


def about(request):
    return render(request, "blog/about.html")
