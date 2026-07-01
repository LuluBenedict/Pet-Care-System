"""
URL configuration for Petcare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
#from django.urls import path, include
#from appointments import views as appointment_views
##from pets import views as pet_views
#from client import views as client_views
#from service import views as service_views

#urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('appointments/', include('appointments.urls')),
    #path('pets/', include('pets.urls')),
    #path('client/', include('client.urls')),
    #path('service/', include('service.urls')),
#]
# Inside petcare/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('client.urls')),

    path('appointments/', include('appointments.urls')),
    path('pets/', include('pets.urls')),
    path('service/', include('service.urls')),
]