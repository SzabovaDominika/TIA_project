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


def index(request):
    pass


def counter_kviz(request):  # req1
    user = request.user.id
    kvizy = Kviz_def.objects.filter(user=user)
    return JsonResponse({'poc_kvizov': len(kvizy)})


def counter_pokus(request):  # req2
    user = request.user.id
    pokusy = Pokus.objects.filter(user=user)
    return JsonResponse({'poc_pokusov': len(pokusy)})


def get_uspesnot(request):  # req3
    user = request.user.id
    pokusy = Pokus.objects.filter(user=user)
    jsonObj = []

    for pk in pokusy:
        val = pk.pokus_body_zisk / pk.pokus_body_max * 100
        jsonObj.append( val)

    return JsonResponse({'stat': jsonObj})

def new_Link(request): #req4

    user = request.user.id

    l = Links()
    l.user = user
    l.link = request.GET['link']
    l.show_as = request.GET['tag']
    l.save()

def all_Link(request): #req5
    user = request.user.id

    linky = Links.objects.filter(user = user)

    jsonObj = {}
    for l in linky:
        jsonObj.update({l.show_as: l.link })

    return JsonResponse(jsonObj)

