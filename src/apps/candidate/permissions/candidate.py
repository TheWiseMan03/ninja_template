from lib.permissions import BasePermission


class IsAdminUser(BasePermission):
    def has_permission(self, request, user):
        return user.is_superuser


class IsStaffUser(BasePermission):
    def has_permission(self, request, user):
        return user.is_staff
