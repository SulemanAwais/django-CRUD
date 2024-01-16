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

from EMS.views import ems_root
from playground.views import root, list_dummy_users, landing_page, create_task, update_task, delete_task, login_page, register, logout_page

urlpatterns = [
    path('', root, name='welcome'),
    path('employee-management-system/', ems_root, name='welcome'),
    path('admin/', admin.site.urls),
    path('dummy-users/', list_dummy_users),
    path('landing_page/', landing_page, name='Home'),
    path('create-task/', create_task, name='Create Task'),
    path('update-task/<id>/', update_task, name='Update Task'),
    path('update-task/', update_task),
    path('delete-task/<id>/', delete_task, name='Delete Task'),
    path('login/', login_page, name='User Login'),
    path('logout/', logout_page),
    path('register/', register, name='Register user'),
]
