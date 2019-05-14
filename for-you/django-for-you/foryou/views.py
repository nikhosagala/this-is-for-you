from django.conf import settings
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings

from foryou.permissions import IsOwnerOrAdmin
from foryou.serializers import UserRegisterSerializer, UserProfileSerializer, UserUpdateSerializer


def version(request):
    return JsonResponse({'apiVersion': settings.API_VERSION})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                return Response({'token': token}, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_409_CONFLICT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        if kwargs.get('pk') == 'me':
            instance = request.user
        else:
            instance = self.get_object()

        partial = kwargs.pop('partial', False)
        serializer = UserUpdateSerializer(instance, data=request.data, partial=partial)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        return Response({'message': 'Not implemented.'}, status=status.HTTP_501_NOT_IMPLEMENTED)

    def retrieve(self, request, *args, **kwargs):
        if kwargs.get('pk') == 'me':
            instance = request.user
        else:
            instance = self.get_object()
        serializer = self.get_serializer(instance=instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

    def get_permissions(self):
        permission_classes = []
        if self.action == 'list':
            permission_classes = [IsAdminUser]
        if self.action in ['retrieve', 'destroy', 'update']:
            permission_classes = [IsOwnerOrAdmin]

        return [permission() for permission in permission_classes]
