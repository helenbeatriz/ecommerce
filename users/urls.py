from django.urls import path
from . import views

urlpatterns = [
    path("", views.users, name="users"),
    path("order_history/<order_number>", views.order_history, name="order_history"),
]
