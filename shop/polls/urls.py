from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('check_user/', views.check_user, name='check_user'),
    path('redirected/', views.redirected, name='redirected'),
    path('registration/', views.registration, name='registration'),
    path('registration/create/', views.create, name='create'),
]