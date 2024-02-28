from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('view/', views.my_view, name='my_view'),
]