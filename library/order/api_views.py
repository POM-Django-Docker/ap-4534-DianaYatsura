from rest_framework import viewsets, permissions

from .models import Order
from .serializers import OrderSerializer


class OrderView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = Order.objects.all()
        # If accessed via nested route /api/v1/user/{user_pk}/order/
        user_pk = self.kwargs.get('user_pk')
        if user_pk is not None:
            queryset = queryset.filter(user__pk=user_pk)
        return queryset

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
