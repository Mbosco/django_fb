from django.db import models
from django_facebook.models import FacebookProfileModel


class MyCustomProfile(FacebookProfileModel):
    user = models.OneToOneField('auth.User')

from django.contrib.auth.models import User
from django.db.models.signals import post_save


def create_facebook_profile(sender, instance, created, **kwargs):
    if created:
        MyCustomProfile.objects.create(user=instance)

post_save.connect(create_facebook_profile, sender=User)