from django.urls import path
from .views import version

app_name = 'foryou'

urlpatterns = [
    path('version', version),
]
