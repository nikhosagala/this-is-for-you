from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

from users.views import version

urlpatterns = [
    path('', include('users.urls')),
    path('auth/login', obtain_jwt_token),
    path('version', version)
]
