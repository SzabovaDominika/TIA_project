from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import sqlite3
from .models import *

# Django showrtcut function https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/
# Elements properties https://javascript.info/size-and-scroll (padding, border, ...)

def index(request):
    # return "aaa"
    # kv1 = Kviz_def()
    # kv1.kviz_nazov = "testovaci kviz 1"
    # kv1.kviz_typ = "Skuska"
    # kv1.kviz_predmet = "Predmet 1"
    # kv1.save()
    # kv = Kviz_def.objects.get(id=1)
    #
    # kv2 = Kviz_def()
    # kv2.kviz_nazov = "Testovaci kviz 2"
    # kv2.kviz_typ = "Zapocet"
    # kv2.kviz_predmet = "Predmet 2"
    # kv2.save()
    #
    # kv3 = Kviz_def()
    # kv3.kviz_nazov = "Testovaci kviz 3"
    # kv3.kviz_typ = "Skuska"
    # kv3.kviz_predmet = "Predmet 3"
    # kv3.save()
    #
    #
    # ot1 = Otazka_def(kviz_id=kv, otazka_znenie = "Kolko percent obzvatelstva sveta su lavaci?")
    # ot1.save()
    # ot2 = Otazka_def(kviz_id=kv, otazka_znenie="Oko pstrosa je vacsie ako jeho mozog.")
    # ot2.save()
    # ot3 = Otazka_def(kviz_id=kv, otazka_znenie="Aka pricut zmrzliny je najoblubenejsia v USA?")
    # ot3.save()
    #
    # odp11 = Odpoved_def(otazka_id=ot1, odpoved_znenie = "viac nez 20%", odpoved_body=0, odpoved_spravna=False)
    # odp11.save()
    # odp12 = Odpoved_def(otazka_id=ot1, odpoved_znenie="20%", odpoved_body=0, odpoved_spravna=False)
    # odp12.save()
    # odp13 = Odpoved_def(otazka_id=ot1, odpoved_znenie="11%", odpoved_body=10, odpoved_spravna=True)
    # odp13.save()
    # odp14 = Odpoved_def(otazka_id=ot1, odpoved_znenie="menej nez 11%", odpoved_body=0, odpoved_spravna=False)
    # odp14.save()
    #
    # odp21 = Odpoved_def(otazka_id=ot2, odpoved_znenie="Loz", odpoved_body=0, odpoved_spravna=False)
    # odp21.save()
    # odp22 = Odpoved_def(otazka_id=ot2, odpoved_znenie="Pravda", odpoved_body=10, odpoved_spravna=True)
    # odp22.save()
    #
    # odp31 = Odpoved_def(otazka_id=ot3, odpoved_znenie="vanilka", odpoved_body=10, odpoved_spravna=True)
    # odp31.save()
    # odp32 = Odpoved_def(otazka_id=ot3, odpoved_znenie="cokolada", odpoved_body=0, odpoved_spravna=False)
    # odp32.save()

    return render(request, 'moje_kvizy.html')
    # return render(request, 'MenuBar.html')

def kviz(request):
    idcko = request.GET['kviz_id']
    return render(request, 'kviz.html', {'kviz_id' : idcko})

def moje_kvizy(request):
    return render(request, 'moje_kvizy.html')

def vysledky(request):
    return render(request, 'kviz_vysledky.html')