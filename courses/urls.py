from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.coursespage, name='coursespage'),
    path('temp/', views.coursetemp, name='coursetemp'),
]