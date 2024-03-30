"""
URL configuration for swingchess project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.contrib.auth import views as auth_views
from swingchess import models
from swingchess import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', models.login, name='login'),
    path('api/check_id/', models.check_id, name='check_id'),
    path('api/register/', models.register, name='register'),
    path('api/logout/', auth_views.LoginView.as_view, name= 'logout'),
    path('log/', views.log_message, name='log_message'),
]
