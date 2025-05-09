from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('destination/<int:pk>/', views.destination_detail, name='destination_detail'),
]