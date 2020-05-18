from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import sqlite3
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *

from .models import *

def index(request):
    pass

def get_all_pokus(request):      #req4
    # query to get all the 'pokus' elements from the DB
    user = request.user.id
    pokusy_all = Pokus.objects.filter(user = user)
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