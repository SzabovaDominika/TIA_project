from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import sqlite3
from django.http import JsonResponse

from .models import *

def index(request):
    pass

def get_all_pokus(request):      #req4
    # query to get all the 'pokus' elements from the DB
    pokusy_all = Pokus.objects.all()
    pokusy = {}
    for pk in pokusy_all:
        kviz = pk.kviz_id
        # kviz = Kviz_def.objects.get(id = kviz_id)
        # pokusy[obj.id] = [kviz.kviz_nazov, kviz.kviz_predmet, kviz.kviz_typ, obj.pokus_datum]
        pokusy[pk.id] = [kviz.kviz_nazov, kviz.kviz_predmet, kviz.kviz_typ, pk.pokus_datum, kviz.id]
    return JsonResponse(pokusy)

def delete_pokus(request):
    idcko = request.GET['pokus_id']
    print("delete pokus idcko:", idcko)
    # Kviz_def.objects.get(id=idcko).delete()
    Pokus.objects.get(id=idcko).delete()

    return True