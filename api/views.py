from django.contrib.auth.models import User
from rest_framework import viewsets

from api.serializers import UserSerializer, ProfileSerializer, KweetSerializer
from logic.models import Profile, Kweet


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class KweetViewset(viewsets.ModelViewSet):
    queryset = Kweet.objects.all()
    serializer_class = KweetSerializer