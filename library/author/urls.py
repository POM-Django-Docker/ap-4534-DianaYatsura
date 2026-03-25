from django.urls import path, include
from rest_framework import routers
from . import views, api_views

router = routers.DefaultRouter()
router.register(r'author', api_views.AuthorView)

app_name = 'author'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('update/<int:author_id>/', views.update, name='update'),
    path('delete/<int:author_id>/', views.delete, name='delete'),
]

api_patterns = [
    path('', include(router.urls)),
]