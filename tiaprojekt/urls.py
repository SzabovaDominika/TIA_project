"""tiaprojekt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views, kviz_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('kviz', views.kviz, name='kviz'),
    path('moje_kvizy', views.moje_kvizy, name = 'moje_kvizy'),
    path('vysledky', views.vysledky, name = 'vysledky'),

    path('kviz_req1', kviz_api.get_otazky),
    path('kviz_req2', kviz_api.add_pokus),
    path('kviz_req3', kviz_api.get_kviz_info),
    path('kviz_req4', kviz_api.get_all_kviz),
    path('kviz_req5', kviz_api.delete_kviz),
    path('kviz_req6', kviz_api.assign_pokus),
    path('kviz_req7', kviz_api.check_odpoved),
    path('vytvor_kvizy', views.vytvor_kvizy),
]
