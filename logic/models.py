from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    screenname = models.CharField(max_length=64)
    bio = models.CharField(max_length=256, null=True, blank=True)
    website = models.CharField(max_length=256, null=True, blank=True)
    location = models.CharField(max_length=256, null=True, blank=True)
    liked_kweets = models.ManyToManyField('Kweet', related_name="liked_by", blank=True)
    follows = models.ManyToManyField('Profile', 'followers', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)


    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.screenname


class Kweet(models.Model):
    message = models.TextField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name="kweets")

    def __str__(self):
        return self.message
