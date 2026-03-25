from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from .models import Author
from .serializers import AuthorSerializer

class HasAuthorEditorRole(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role >= 1

class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = "pk"

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [permissions.AllowAny()]
        return [HasAuthorEditorRole()]

    def destroy(self, request, *args, **kwargs):
        author = self.get_object()
        if author.book_set.exists():
            return Response({"detail": f"Could not delete: {author.surname} is linked to books."},
                            status=status.HTTP_400_BAD_REQUEST)
        return super().destroy(request, *args, **kwargs)