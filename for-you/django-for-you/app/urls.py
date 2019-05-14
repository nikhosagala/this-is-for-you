from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('', include('foryou.urls')),
    path('auth/login', obtain_jwt_token)
]
