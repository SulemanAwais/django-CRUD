from django.urls import path
from playground.views import (
    RootView,
    ListDummyUsersView,
    LandingPageView,
    CreateTaskView,
    UpdateTaskView,
    DeleteTaskView,
    RegisterView,
    LoginPageView,
    LogoutPageView
)

urlpatterns = [
    path('', RootView.as_view(), name='root'),
    path('dummy-users/', ListDummyUsersView.as_view(), name='list_dummy_users'),
    path('landing_page/', LandingPageView.as_view(), name='landing_page'),
    path('create-task/', CreateTaskView.as_view(), name='create_task'),
    path('update-task/<int:id>/', UpdateTaskView.as_view(), name='update_task'),
    path('delete-task/<int:id>/', DeleteTaskView.as_view(), name='delete_task'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', LogoutPageView.as_view(), name='logout'),
]
