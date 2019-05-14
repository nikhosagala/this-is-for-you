from django.urls import path, include
from rest_framework import routers

from foryou.views import UserViewSet, version

app_name = 'foryou'

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('version', version),
]
