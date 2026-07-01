from django .urls import path
from . import views

#urlpatterns = [
    #path('pets/',views.pet_list, name='pet_list')
#]
urlpatterns = [
    path('', views.pet_list, name='pet_list'),
]