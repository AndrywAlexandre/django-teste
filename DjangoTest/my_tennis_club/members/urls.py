from django.urls import path
from members import views
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
]