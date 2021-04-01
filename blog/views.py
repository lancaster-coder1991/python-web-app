# The render built-in function takes the request as a first argument, then a file path to templates as its second argument.
# The teampltes are HTML files which will display when a particular view is routed to, if the render function has been invoked correctly.
from django.shortcuts import render

# We can use the below syntax to import models from the current directory
from .models import Post

# We can use the HttpResponse function from django.http to create content to send to the client when they hit a particular route
# NB this is only needed when templates aren't being used.
from django.http import HttpResponse


posts = [  # This data is akin to the format that using object methods such as Post.objects.all() will return
    {
        "author": "CoreyMS",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "August 27, 2018",
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "August 28, 2018",
    },
]


def home(request):
    # We can add a context dictionary with values that relate to data to pass to our templates
    context = {"posts": Post.objects.all()}

    # No need to add /templates to the directory filepath here, as Django automatically loks in this folder for templates
    # Notice that context has been added as the third argument to the render method
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
