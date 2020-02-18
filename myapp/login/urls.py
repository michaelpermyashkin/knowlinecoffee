from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from login.views import (
    signin,
)

urlpatterns = [
    path('signup/', views.signup, name='login-signup'),
    path('signout/', views.signout, name='login-signout'),
    path('login/', views.signin, name = "login-signin"),
]