from django.contrib.auth.models import User
from rest_framework import serializers

from logic.models import Profile, Kweet


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class SimpleProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('screenname', 'id')


class SimpleKweetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kweet
        fields = ('id', 'message', 'created')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    follows = SimpleProfileSerializer(many=True, read_only=True)
    followers = SimpleProfileSerializer(many=True, read_only=True)
    kweets = SimpleKweetSerializer(many=True, read_only=True)
    liked_kweets = SimpleKweetSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ('screenname', 'id', 'follows', 'followers', 'kweets', 'liked_kweets')


class KweetSerializer(serializers.HyperlinkedModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Kweet
        fields = ('id', 'message', 'created', 'last_edited', 'profile')
