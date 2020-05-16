from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
import sqlite3
from django.contrib.auth.forms import UserCreationForm

from .models import *
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Django showrtcut function https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/
# Elements properties https://javascript.info/size-and-scroll (padding, border, ...)

def register(request):
    if request.user.is_authenticated:
        return redirect('nastenka')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'KONTO VYTOVRENÉ PRE POUŽÍVATEĽA ' + user)
                return redirect('nastenka')
        context = {'form': form}
        return render(request, 'register.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('nastenka')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('nastenka')
            else:
                messages.info(request, 'MENO ALEBO HESLO JE NESPRÁVNE')
        context = {}
        return render(request, 'login.html', context)


def nastenka(request):
    # uname = request.GET['uname']
    # return render(request, 'Nastenka.html', {'uname': uname})
    return render(request, 'Nastenka.html')


def kviz(request):
    idcko = request.GET['kviz_id']
    return render(request, 'kviz.html', {'kviz_id': idcko})


def moje_kvizy(request): #FUNGUJE REDIRECT AJ KONTROLA!
    # if request.user.is_authenticated:
    #     return render(request, 'moje_kvizy.html')
    # else:
    #     return redirect('login')

    return render(request, 'moje_kvizy.html')


def historia_pokusov(request):
    return render(request, 'historia_pokusov.html')


def o_appke(request):
    return render(request, 'oAppke.html')


def vysledky(request):
    kviz_id = request.GET['kviz_id']
    pokus_id = request.GET['pokus_id']
    return render(request, 'kviz_vysledky.html', {'kviz_id': kviz_id, 'pokus_id': pokus_id})


def vytvor_kviz(request):
    return render(request, 'vytvor_kviz.html')


def pridaj_otazku(request):
    idcko = request.GET['kviz_id']
    return render(request, 'pridaj_otazku.html', {'kviz_id': idcko})


def edituj_kviz(request):
    idcko = request.GET['kviz_id']
    return render(request, 'edituj_kviz.html', {'kviz_id': idcko})
