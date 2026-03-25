from rest_framework import viewsets, permissions
from .models import CustomUser
from .serializers import UserSerializer

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user or request.user.is_staff or request.user.is_superuser

class UserView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        if self.action == 'list':
            return [permissions.IsAuthenticated()]

        return [permissions.IsAuthenticated(), IsOwnerOrReadOnly()]

