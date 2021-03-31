# In the models.py file, we define classes which make up the data in the database that Django is connected to. Each class represents a type of information, sort of equivalent to what you would call different SQL tables in an SQL DB

from django.db import models
from django.utils import (
    timezone,
)  # this utility is used below when creating an automatic datestamp against the date_posted field of each post


class Post(
    models.Model
):  # each class will be its own table (Model) in the database via this inheritance
    title = modles.CharField(max_length=100)  # CharField representes a string field
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
