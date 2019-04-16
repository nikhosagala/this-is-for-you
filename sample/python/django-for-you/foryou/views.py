from django.conf import settings
from django.http import JsonResponse


def version(request):
    return JsonResponse({'apiVersion': settings.API_VERSION})
