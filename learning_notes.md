## General Notes

Django projects can contain multiple apps within the same project. For example, a website might have a store, a blog and a members area, all of which can be different apps in the code.

Apps need to be added into the INSTALLED_APPS array found in djangoproject/settings.py. The syntax for the entry is a string in the form "app name".apps."app config name", where "app config name is the name of the App class found in "app name"/apps.py. E.g.:

"blog.apps.BlogConfig"

Static files such as CSS and JS files are typically kept within a 'static' directory within each app.

## Routing

Routing for the project is managed through the central django_project urls.py file. When someone navigates to a path on the project server, the request is sent to this file. If a matching path is found, redirection to the appropriate path and code will take place.

For example, this is sample code from the django_project urls.py file:

    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path("admin/", admin.site.urls),
        path("blog/", include("blog.urls")),
    ]

What this means is that if someone navigates to /admin, take them to the default admin page that comes with a new Django project. If they navigate to /blog, take them to them blog.urls file in this project for further redirection. Note the importing and invocation of the include function - this will essentially chop the /blog from the path and pass the remaining path to the blogs.url file.

The blog.urls file within the blog app looks like this:

    from django.urls import path
    from . import views

    urlpatterns = [
        path("", views.home, name="blog-home"),
    ]

This means that when no further route has been supplied beyond /blog, display the contents of the return value of the home component in the views.py file in the blog directory.

## Templates

Temapltes are used to create HTML snippets to be inserted into route functions. Djangon automatically looks for a 'templates/"app name"' directory in each app folder where these snippets should be kept. Each template is an HTML file. See the templates directory and views.py within blog for more info on how to pass variables to the HTML.

To avoid repeated code between templates, you can use template inheritance.

## CLI

Use the commands below when creating new apps within this project directory:

To run a the project server:

    python manage.py runserver

To start a new App within the project

    python manage.py startapp <name of app>
