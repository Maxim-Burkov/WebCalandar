from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('regging/', views.regging, name='regging'),
    path('create/', views.create, name='create'),
    path('<int:id>/', views.standart_profile, name='standart_profile'),
    path('create_event/', views.create_event, name='create_event'),
    path('create_event/check_event', views.check_event, name='check_event'),
    path('redacting/<int:id>/', views.redacting, name='redacting'),
    path('deleteevent/<int:id>/', views.delete_event, name='delete_event'),
    path('redactingevent/<int:id>', views.redacting_event, name='redacting_event'),
]