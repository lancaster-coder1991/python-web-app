# In the models.py file, we define classes which make up the data in the database that Django is connected to. Each class represents a type of information, sort of equivalent to what you would call different SQL tables in an SQL DB

from django.db import models
from django.utils import (
    timezone,
)  # this utility is used below when creating an automatic datestamp against the date_posted field of each post
from django.contrib.auth.models import (
    User,
)  # Here we are importing in information from the administrative Users table to link to this table


class Post(
    models.Model
):  # each class will be its own table (Model) in the database via this inheritance
    title = models.CharField(max_length=100)  # CharField representes a string field
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # the on_delete argument is stating that if the user of a post is deleted, their posts should be deleted as well

    def __str__(
        self,
    ):  # Via this dunder method, we can change what appears in the shell when inspecting entries into this model
        return self.title