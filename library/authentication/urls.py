from django.urls import path, include
from rest_framework_nested import routers
from . import views, api_views

router = routers.DefaultRouter()
router.register(r'user', api_views.UserView)

app_name = 'user'

urlpatterns = [
    path('users/', views.user_list_view, name='index'),
    path('<int:user_id>/', views.user_detail_view, name='detail'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

api_patterns = [
    path('', include(router.urls)),
]