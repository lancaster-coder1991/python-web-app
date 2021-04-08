from django.db import models
from django.contrib.auth.models import (
    User,
)  # In the Profile model, we want to set up a 1-1 relationship with each user on the DB - see below for how this is implemented
from PIL import Image


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

    # def save(
    #     self, *args, **kwargs
    # ):  # All models have a default save method, but this can be overwritten as here
    #     super().save(
    #         *args, **kwargs
    #     )  # We still want to run the saving functionality from the default save function
    #     img = Image.open(
    #         self.image.path
    #     )  # Using the Image class imported from Pillow, we can open and resize user uploaded images using its path
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)


# Create your models here.
