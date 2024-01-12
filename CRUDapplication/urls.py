"""
URL configuration for CRUDapplication project.

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
from django.urls import path, include
from playground.views import list_dummy_users, landing_page, create_task, update_task, delete_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dummy-users/', list_dummy_users),
    path('', landing_page),
    path('create-task/', create_task),
    path('update-task/<id>/', update_task),
    path('update-task/', update_task),
    path('delete-task/<id>/', delete_task),
]
