from django.db import models
from django.contrib.auth.models import (
    User,
)  # In the Profile model, we want to set up a 1-1 relationship with each user on the DB - see below for how this is implemented


class Profile(
    models.Model
):  # When creating a new class of item to eb stored on our db, it always inherits from models.Model
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )  # The models OneToOneField method denotes a 1-1 relationship between two models.
    image = models.ImageField(
        default="default.png", upload_to="profile_pics"
    )  # In conjunction with the MEDIA_ROOT and MEDIA_URL settings in settings.py, pictures uploaded to user accounts will be uploaded to /media/profile_pics

    def __str__(self):
        return f"{self.user.username}'s Profile"


# Create your models here.
