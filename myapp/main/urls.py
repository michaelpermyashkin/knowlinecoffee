from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main-home'),
    path('update-options/', views.update_options, name='main-update-options'),
    path('request-options/', views.request_options, name='main-request-options'),
    path('request-sent/', views.request_sent, name='main-request-sent'),
    path('starbucks/', views.starbucks, name='main-update-starbucks'),
    path('dunkin/', views.dunkin, name='main-update-dunkin'),
    path('offline/', views.offline, name='main-offline'),

    path('location-denied/', views.location_denied, name="location-denied"),
    path('location-unavailable/', views.location_unavailable, name="location-unavailable"),
    path('location-invalid/', views.location_invalid, name="location-invalid"),
]