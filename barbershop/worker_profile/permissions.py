from rest_framework.permissions import BasePermission, SAFE_METHODS


class WorkerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.worker.position == 'admin':
            return True
        return obj.worker_profile.worker == request.user
