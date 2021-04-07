# The render built-in function takes the request as a first argument, then a file path to templates as its second argument.
# The teampltes are HTML files which will display when a particular view is routed to, if the render function has been invoked correctly.
from django.shortcuts import render

# We can use the below syntax to import models from the current directory
from .models import Post

# We can use the HttpResponse function from django.http to create content to send to the client when they hit a particular route
# NB this is only needed when templates aren't being used.
from django.http import HttpResponse

from django.views.generic import ListView


# NB this function view or home is not being used - the class view below is currently used. Kept this one in for reference
def home(request):
    # We can add a context dictionary with values that relate to data to pass to our templates
    context = {"posts": Post.objects.all()}

    # No need to add /templates to the directory filepath here, as Django automatically loks in this folder for templates
    # Notice that context has been added as the third argument to the render method
    return render(request, "blog/home.html", context)


# Below is an example of using predefined class views rather than function views. We create a new class that inherist from one of the generic view classes provided by Django
class PostListView(ListView):
    model = Post  # This tells the view what model to query in order to create the List
    # By default, class views will try to load templates found at "app name"/"model name (in this case 'post'"_"viewtype"(in this case list).html - so in this example that would be blog/post_list.html
    # We can overwrite this behaviour as below
    template_name = "blog/home.html"
    context_object_name = "posts"  # This overrides the default


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
