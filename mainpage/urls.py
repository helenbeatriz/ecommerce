from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls import handler500

handler500 = 'mainpage.views.server_error'

urlpatterns = [
    path('', views.index, name='mainpage'),
    path('403/', views.error_403, name='403'),
    path('400/', views.bad_request, name='bad_request'),
]
