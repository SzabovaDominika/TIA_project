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
from . import views, kviz_api, history_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='home_login'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('kviz', views.kviz, name='kviz'),
    path('moje_kvizy', views.moje_kvizy, name='moje_kvizy'),
    path('vysledky', views.vysledky, name='vysledky'),
    path('historia_pokusov', views.historia_pokusov, name='historia_pokusov'),
    path('oappke', views.o_appke),
    path('nastenka', views.nastenka, name='nastenka'),

    # Requestes related to KVIZ model administration
    path('kviz_req1', kviz_api.get_otazky),
    path('kviz_req2', kviz_api.add_pokus),
    path('kviz_req3', kviz_api.get_kviz_info),
    path('kviz_req4', kviz_api.get_all_kviz),
    path('kviz_req5', kviz_api.delete_kviz),
    path('kviz_req6', kviz_api.assign_pokus),
    path('kviz_req7', kviz_api.add_odpoved),
    path('kviz_req8', kviz_api.createnew_kviz),
    path('kviz_req9', kviz_api.add_new_question_definition),
    path('kviz_req10', kviz_api.add_new_answer_definition),
    path('kviz_req11', kviz_api.edit_kviz),
    path('kviz_req12', kviz_api.delete_otazka),
    path('kviz_req13', kviz_api.get_pokus_vysledok),

    # Render windows
    path('vytvor_kviz', views.vytvor_kviz),
    path('pridaj_otazku', views.pridaj_otazku),
    path('history', history_api.get_all_pokus),
    path('edituj_kviz', views.edituj_kviz),

    # Requestes related to POKUS model administration
    path('history_req1', history_api.delete_pokus)
]
