from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

from api.views import UserViewset, ProfileViewset, KweetViewset

router = routers.DefaultRouter()
router.register(r'users', UserViewset)
router.register(r'profiles', ProfileViewset)
router.register(r'kweets', KweetViewset)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/login/', obtain_jwt_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]