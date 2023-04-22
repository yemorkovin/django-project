"""final_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from yourphoto import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('auto/', views.auto, name='auto'),
    path('contacts/', views.contacts, name='contacts'),
    path('registration/', views.registration, name='registration'),
    path('exit/', views.exit, name='exit'),
    path('filter/', views.filter, name='filter'),
    path('filter/user/', views.user, name='user'),
    path('panel/', views.panel, name='panel'),
    path('add_photo/', views.add_photo, name='add_photo'),
    path('delete/', views.delete, name='delete'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)