from django.urls import path, include
from rest_framework import routers

from users.views import UserViewSet, version

app_name = 'users'

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
