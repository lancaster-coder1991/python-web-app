from django.contrib import admin
from .models import (
    Post,
)  # Tor egister a model to view it on the admin page, you need to import it in

admin.site.register(
    Post
)  # Syntax for registering a Model for viewing on the admin page
