from django.contrib.auth.models import User
from rest_framework import viewsets, pagination, permissions
from rest_framework.response import Response

from api.serializers import UserSerializer, ProfileSerializer, KweetSerializer
from logic.models import Profile, Kweet


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAdminUser]

    def create(self, request, *args, **kwargs):
        return Response(status=405)

    def get_permissions(self):
        if self.action in ['destroy', 'create']:
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]

        return [perm() for perm in permission_classes]


class KweetViewset(viewsets.ModelViewSet):
    queryset = Kweet.objects.all()
    serializer_class = KweetSerializer
    pagination_class = pagination.LimitOffsetPagination

    def get_permissions(self):
        if self.action in ['destroy']:
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]

        return [perm() for perm in permission_classes]

    def list(self, request, *args, **kwargs):
        user = request.user.profile
        kweets = Kweet.objects.filter(profile__in=user.follows.all())
        serializer = KweetSerializer(kweets, many=True)
        return Response(serializer.data)
