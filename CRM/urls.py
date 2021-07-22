"""CRM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from django.urls.conf import include

from .views import *

from crmapp.views import CreateEnquiry

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', CustomRegister.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('api/', include('crmapp.urls')),
    path('createenquiry/', CreateEnquiry.as_view(), name='create')
]