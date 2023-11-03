from rest_framework.permissions import BasePermission


class HabitsPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        if view.action in ['update', 'retrieve', 'destroy']:
            return request.user == obj.owner