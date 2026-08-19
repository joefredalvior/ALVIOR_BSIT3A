from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('simple/', views.index, name='index'),
]