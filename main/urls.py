
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.apiHome, name='api-home'),
    path('overview/', views.apiOverview, name='api-overview'),
    path('devices/', views.deviceList, name='device-list'),
    path('devices/<str:identifier>', views.deviceDetail, name='device-detail'),

]