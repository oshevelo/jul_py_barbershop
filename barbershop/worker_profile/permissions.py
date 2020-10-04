from rest_framework.permissions import BasePermission, SAFE_METHODS


class WorkerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS and obj.worker_profile.worker == request.user:
            return obj.worker_profile.worker
        elif request.method in SAFE_METHODS and request.worker.position == 'admin':
            return True

