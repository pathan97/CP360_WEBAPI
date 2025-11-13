from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'admin':

class IsStaff(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'staff':

class IsEndUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'end_user':

class IsAgent(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'agent':
