from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import sqlite3

# Django showrtcut function https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/
# Elements properties https://javascript.info/size-and-scroll (padding, border, ...)

def index(request):
    #return HttpResponse("<b>Hello</b>, world. You're at the polls index.")

    #return render(request, 'kviz.html')
    return render(request, 'ActionBar.html')

def kviz(request):
    idcko = request.GET['kviz_id']
    return render(request, 'kviz.html', {'kviz_id' : idcko})

def moje_kvizy(request):
    return render(request, 'moje_kvizy.html')

def vysledky(request):
    return render(request, 'kviz_vysledky.html')