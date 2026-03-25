from django.urls import path, include
from rest_framework import routers
from rest_framework_nested import routers as nested_routers
from authentication.urls import router as user_router
from . import views, api_views

# Standalone router for /api/v1/order/
router = routers.DefaultRouter()
router.register(r'order', api_views.OrderView, basename='order')

# Nested router for /api/v1/user/{user_pk}/order/
order_router = nested_routers.NestedSimpleRouter(user_router, r'user', lookup='user')
order_router.register(r'order', api_views.OrderView, basename='user-order')

app_name = "order"

urlpatterns = [
    path("", views.all_orders, name="index"),
    path("my/", views.my_orders, name="my_orders"),
    path("all/", views.all_orders, name="all_orders"),
    path("create/", views.order_create, name="create"),
    path("<int:pk>/", views.order_detail, name="detail"),
    path("<int:pk>/edit/", views.order_edit, name="edit"),
    path("<int:pk>/delete/", views.order_delete, name="delete"),
]

api_patterns = [
    path('', include(router.urls)),
    path('', include(order_router.urls)),
]
