"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from authentication.urls import api_patterns as auth_api
from author.urls import api_patterns as author_api
from book.urls import api_patterns as book_api
from order.urls import api_patterns as order_api
from .views import home

handler404 = "library.views.custom_404"

urlpatterns = [
    path("", home, name="home"),
    path('admin/', admin.site.urls),
    path('user/', include('authentication.urls', namespace='user')),
    path('author/', include('author.urls', namespace='author')),
    path('books/', include('book.urls', namespace='book')),
    path("orders/", include("order.urls", namespace="order")),
    path('api/v1/', include(auth_api)),
    path('api/v1/', include(author_api)),
    path('api/v1/', include(book_api)),
    path('api/v1/', include(order_api)),
]
