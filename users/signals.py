from django.db.models.signals import post_save  #
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# This means that when a User is saved, the post_save signal will be sent
# The signal will be received by the receiver, which is the function decorated by the @receiver decorator - in this case create_profile
@receiver(post_save, sender=User)
def create_profile(
    sender, instance, created, **kwargs
):  # The receiver function has arguments passed to it from the signal (post_save in this case)
    if created:  # Is the user was created, also create a profile for that user
        Profile.objects.create(user=instance)


# This function saves a user profile every time the associated user is edited and saved
@receiver(post_save, sender=User)
def save_profile(
    sender, instance, **kwargs
):  # The receiver function has arguments passed to it from the signal (post_save in this case)
    instance.profile.save()


# Note that for signals to work, a ready method importing the signals in this file needs to be created in "app name/apps.py"