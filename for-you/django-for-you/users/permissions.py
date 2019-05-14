from rest_framework.permissions import BasePermission


class IsOwnerOrAdmin(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        try:
            permission = bool(request.user and (
                    request.user.is_staff or request.user == obj.user))
        except AttributeError:
            permission = bool(request.user == obj)
        return permission
