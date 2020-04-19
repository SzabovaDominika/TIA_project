from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import sqlite3
from django.http import JsonResponse

from .models import *

def index(request):
    pass

def get_kviz_info(request):  #re3
    idcko = request.GET['kviz_id']
    kviz = Kviz_def.objects.get(id=idcko)
    info = {}
    info['nazov'] = kviz.kviz_nazov
    info['typ'] = kviz.kviz_typ
    info['predmet'] = kviz.kviz_predmet

    return JsonResponse(info)

def get_otazky(request):     # req1

    print("get_otazky   " + request.GET['kviz_id'])

    otazky_odpovede_ids = {}
    idcko = request.GET['kviz_id']
    kviz = Kviz_def.objects.get(id=idcko)
    otazky = Otazka_def.objects.filter(kviz_id=kviz)
    jsonObj = {}
    for att in otazky:
        odpovede = Odpoved_def.objects.filter(otazka_id=att.id).values()
        collection = []
        list = []
        for i in range(len(odpovede)):
            list.append(odpovede[i]['odpoved_znenie'])
            collection.append(odpovede[i]['id'])
        otazky_odpovede_ids[att.id] = collection
        jsonObj[att.otazka_znenie] = list

    jsonObj['id'] = otazky_odpovede_ids
    return JsonResponse(jsonObj)

def assign_pokus(request): #req6
    id_kv = request.GET['kviz_id']

    pokus = Pokus()
    pokus.kviz_id = Kviz_def.objects.get(id=id_kv)
    pokus.pokus_zaciatok = request.GET['zaciatok']
    pokus.pokus_koniec = request.GET['koniec']
    pokus.pokus_datum = request.GET['zaciatok']
    pokus.pokus_neuhadol = 0
    pokus.pokus_uhadol = 0
    pokus.pokus_neodpovedal = 0
    pokus.save()
    print(pokus.pk)

    return JsonResponse({'id': pokus.pk})

def get_all_kviz(request):      #req4
    mnozina = Kviz_def.objects.all()
    kvizy = {}
    print("hejhou")
    for obj in mnozina:
        kvizy[obj.id] = [obj.kviz_nazov, obj.kviz_predmet, obj.kviz_typ, obj.kviz_vytvoreny]
    print(kvizy)
    return JsonResponse(kvizy)

def delete_kviz(request):    #req5


    idcko = request.GET['kviz_id']
    print(idcko)
    Kviz_def.objects.get(id=idcko).delete()
    print(Kviz_def.objects.get(id=idcko))

    return True

def check_odpoved(request):   #req7
    vysledok = {}
    otazka_id = request.GET['otazka_id']
    odpoved_id = request.GET['moja_odpoved_id']
    pokus_id = request.GET['pokus_id']
    print(otazka_id, odpoved_id, pokus_id)
    # zalozime novu odpoved na pokus
    odp = Odpoved()
    odp.otazka_id = Otazka_def.objects.get(id=otazka_id)
    odp.pokus_id = Pokus.objects.get(id=pokus_id)
    odp.odpoved_moja = Odpoved_def.objects.get(id=odpoved_id)
    odp.save()
    # pozbierame vysledky pre funkciu
    odpoved_obj = Odpoved_def.objects.get(id=odpoved_id)
    vysledok['odpoved'] = odpoved_obj.odpoved_spravna
    vysledok['znenie'] = odpoved_obj.odpoved_znenie
    vysledok['body'] = odpoved_obj.odpoved_body

    return JsonResponse(vysledok)

def add_pokus(request):
    #req2
    pokus_id = request.GET['pokus_id']
    pk = Pokus.objects.get(id=pokus_id)
    pk.pokus_neuhadol = request.GET['neuhadol']
    pk.pokus_uhadol = request.GET['udaol']
    pk.pokus_neodpovedal = request.GET['neodpovedal']
    pk.pokus_body = request.GET['body']

    return JsonResponse({0: 'true'})