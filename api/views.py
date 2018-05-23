from django.contrib.auth.models import User
from rest_framework import viewsets, pagination, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from api.serializers import UserSerializer, ProfileSerializer, KweetSerializer
from logic.models import Profile, Kweet


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = permissions.IsAdminUser
    search_fields = ('username', 'id', 'email')


class ProfileViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ('screenname',)
    ordering_fields = ('last_edited', 'created')

    @action(detail=True, methods=['put, delete'])
    def follow(self, request, *args, **kwargs):
        obj = (self.get_object())
        me = request.user

        if request.method == "post":
            if obj not in me.follows:
                me.follows.append(obj)
                me.save()
                return Response(status=200, data=me)
            else:
                return Response(304, data=me)
        else:
            if obj in me.follows:
                me.follows.remove(obj)
                me.save()
                return Response(status=200, data=me)
            else:
                return Response(status=304, data=me)

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
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ('message')
    ordering_fields = ('last_edited', 'created')

    def get_permissions(self):
        if self.action in ['destroy']:
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]

        return [perm() for perm in permission_classes]

    def create(self, request, *args, **kwargs):
        super(self, args, kwargs)

    def list(self, request, *args, **kwargs):
        user = request.user.profile
        kweets = Kweet.objects.filter(profile__in=user.follows.all())
        serializer = KweetSerializer(kweets, many=True)
        return Response(serializer.data)

    @action(methods=['put', 'delete'], detail=True)
    def like(self, request, *args, **kwargs):
        me = request.user
        kweet = self.get_object()

        if request.method == 'put':
            if kweet not in me.likes:
                me.likes.append(kweet)
                me.save()
                return Response(status=200, data=kweet)
            else:
                return Response(status=304, data=kweet)
        else:
            if kweet in me.likes:
                me.likes.removes(kweet)
                me.save()
                return Response(status=200, data=kweet)
            else:
                return Response(status=304, data=kweet)

