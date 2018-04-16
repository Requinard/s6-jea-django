from django.db import models


# Create your models here.
class Profile(models.Model):
    screenname = models.CharField(max_length=64)
    bio = models.CharField(max_length=256, null=True, blank=True)
    website = models.CharField(max_length=256, null=True, blank=True)
    location = models.CharField(max_length=256, null=True, blank=True)
    likes = models.ManyToManyField('Kweet', related_name="liked_kweets")
    follows = models.ManyToManyField('Profile', 'followers')

class Kweet(models.Model):
    message = models.TextField(max_length=256)
    created = models.DateTimeField(auto_now=True)
    last_edited = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
