from django.urls import path
from .import views

#urlpatterns = [
   # path('appointments/', views.appointment_list, name='appointment_list')
#]
urlpatterns = [
    path('', views.appointment_list, name='appointment_list'),
]