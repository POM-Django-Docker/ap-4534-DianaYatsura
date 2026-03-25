from django.urls import path, include
from rest_framework import routers
from . import views, api_views

router = routers.DefaultRouter()
router.register(r'book', api_views.BookView)

app_name = "book"

urlpatterns = [
    path('', views.book_list, name='index'),
    path('<int:pk>/', views.book_detail, name='book_detail'),
    path('create/', views.book_create, name='book_create'),
    path('<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('<int:pk>/delete/', views.book_delete, name='book_delete'),
]

api_patterns = [
    path('', include(router.urls)),
]