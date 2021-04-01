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

## Database

Django has a built in ORM (Object Relational Mapper). This emans that we can access databases in an object-orientated way.

## Admin Page

By default, the /admin path of your project navigates to a default Django admin portal. Via this portal you can editview and edit the data that your site uses in a GUI. You can also create additional admin users here once the first has been created via the CLI (see below).

Once data has been created on the database, you need to register it on the admin page. This can be done via the admin.py file in the app directory - see the example in the blog admin.py file for the syntax for this.

## CLI

Use the commands below when creating new apps within this project directory:

To run a the project server:

    python manage.py runserver

To start a new App within the project:

    python manage.py startapp <name of app>

These commands create a new database and migrate some default tables to it if you don't have a DB set up. If you have set one up, then makemigrations command will add migration classes to "app name/migrations" in separate files. The migrate command will actually run the migrations:

    python manage.py makemigrations
    python manage.py migrate

To check SQL code that will be run on a migration after 'makemigration' has been run to create the migration class, use this command:

    python manage.py sqlmigrate *name of app* *number of migration*
    e.g.: python manage.py sqlmigrate blow 0001

To create a new user to log into /admin page of the project (NB this requird a database to work, see above):

    python manage.py createsuperuser

To open a python/django shell:

    python manage.py shell

## Django Shell

Using the above comamnd we can open a shell that lets us experiment with data easily. In the shell we need to import any entities we want to experiemnt with, using the same syntax as in a .py file:

    from blog.models import Post
    from django.contrib.auth.models import User

Then we can access pieces of information using dot notation and methods:

    User.objects.all() //Selects all entries in the User table
    User.objects.fiest() //Selects the first entry - note that first() also unpacks the entry from the array, rather than returning a single-element array
    User.objects.filter(username='george.scott')

Entries found using the above kind of methods can be assigned to variables using standard python syntax:

    user = User.objects.get(id=1)

We can create new objects for our tables using class contructor syntax:

    post_1 = Post(title="Blog 1", content='First Post Content!', author=user)

Note that the above new object needs saving into the DB:

    post_1.save()

One we have selected entried from a model, we can run queries on them using ethods provided to us by Django:

    user = User.objects.get(id=1)
    post = user.post_set // finds all posts for this user using _set
    user.post_set.all() // lists all results of above
    user.post_set.create(title='Blog 3', content='Third Post Content!')  // creates a new post for this user
