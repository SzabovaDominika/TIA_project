from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import sqlite3
from django.http import JsonResponse

from .models import *


def index(request):
    pass


def get_otazky(request):  # req1
    otazky_odpovede_ids = {}
    idcko = request.GET['kviz_id']
    kviz = Kviz_def.objects.get(id=idcko)
    otazky = Otazka_def.objects.filter(kviz_id=kviz)

    jsonObj = {}
    jsonObj['id'] = idcko
    for i in range(len(otazky)):
        ot = otazky[i]
        odpovede = Odpoved_def.objects.filter(otazka_id=ot.id).values()
        jsonObj[i] = {0: [ot.id, ot.otazka_znenie]}
        for j in range(len(odpovede)):
            odp = odpovede[j]
            jsonObj[i].update({j+1: [odp['id'], odp['odpoved_znenie'],
                                     odp['odpoved_body'], odp['odpoved_spravna']]})
    return JsonResponse(jsonObj)


def add_pokus(request):
    # req2
    pokus_id = request.GET['pokus_id']
    pk = Pokus.objects.get(id=pokus_id)
    pk.pokus_neuhadol = request.GET['neuhadol']
    pk.pokus_uhadol = request.GET['udaol']
    pk.pokus_neodpovedal = request.GET['neodpovedal']
    pk.pokus_body = request.GET['body']

    return JsonResponse({0: 'true'})


def get_kviz_info(request):  # req3
    idcko = request.GET['kviz_id']
    kviz = Kviz_def.objects.get(id=idcko)
    info = {}
    info['nazov'] = kviz.kviz_nazov
    info['typ'] = kviz.kviz_typ
    info['predmet'] = kviz.kviz_predmet

    return JsonResponse(info)


def get_all_kviz(request):  # req4
    # query to get all the 'kviz' elements from the DB
    mnozina = Kviz_def.objects.all()
    kvizy = {}
    for obj in mnozina:
        kvizy[obj.id] = [obj.kviz_nazov, obj.kviz_predmet, obj.kviz_typ, obj.kviz_vytvoreny]
    return JsonResponse(kvizy)


def delete_kviz(request):  # req5
    idcko = request.GET['kviz_id']
    Kviz_def.objects.get(id=idcko).delete()


def assign_pokus(request):  # req6
    id_kv = request.GET['kviz_id']

    pokus = Pokus()
    pokus.kviz_id = Kviz_def.objects.get(id=id_kv)
    pokus.pokus_zaciatok = request.GET['zaciatok']
    pokus.pokus_koniec = request.GET['koniec']
    pokus.pokus_datum = request.GET['zaciatok']
    pokus.pokus_neuhadol = request.GET['nespravne']
    pokus.pokus_uhadol = request.GET['spravne']
    pokus.pokus_neodpovedal = request.GET['nezodpovedane']
    pokus.save()

    return JsonResponse({'id': pokus.pk})


def add_odpoved(request):  # req7
    pokus_id = request.GET['pokus_id']
    # zalozime novu odpoved na pokus
    odp = Odpoved()
    odp.otazka_id = request.GET['otazka_id']
    odp.pokus_id = Pokus.objects.get(id=pokus_id)
    odp.odpoved_moja = request.GET['moja_odpoved_id']
    odp.save()

def createnew_kviz(request):
    # kviz_req8
    title = request.GET['title']
    lecture = request.GET['lecture']
    typ = request.GET['type']

    newQ = Kviz_def()
    newQ.kviz_nazov = title
    newQ.kviz_predmet = lecture
    newQ.kviz_typ = typ
    newQ.save()

    idcko = newQ.id
    print("new kviz id", idcko)

    return JsonResponse({1: idcko})


def add_new_question_definition(request):
    # req9
    kv_id = request.GET['kviz_id']
    kv_obj = Kviz_def.objects.get(id=kv_id)
    new_ot = Otazka_def()
    new_ot.kviz_id = kv_obj
    new_ot.otazka_znenie = request.GET['otazka_znenie']
    new_ot.save()

    idcko = new_ot.id
    print("new idcko otazka", idcko)
    return JsonResponse({'id': idcko})


def add_new_answer_definition(request):
    # req10

    ot_id = request.GET['otazka_id']
    ot_obj = Otazka_def.objects.get(id=ot_id)

    new_odp = Odpoved_def()
    new_odp.otazka_id = ot_obj
    new_odp.odpoved_znenie = request.GET['znenie']
    new_odp.odpoved_body = request.GET['body']

    spravna = request.GET['spravna']
    print("SPRAVNOST OTAZKY: ", spravna)
    if spravna == 'true':
        print("odpoved je spravna")
        new_odp.odpoved_spravna = True
    else:
        print("odpoved je nespravna")
        new_odp.odpoved_spravna = False

    new_odp.save()
    print("new idcko odpoved", new_odp.id)
    print("new idcko odpoved", new_odp.odpoved_spravna)


def edit_kviz(request):
    #req11
    kvid = request.GET['kviz_id']
    title = request.GET['title']
    lecture = request.GET['lecture']
    typ = request.GET['type']

    kv = Kviz_def.objects.get(id = kvid)

    if title != "": kv.kviz_nazov = title
    if lecture != "": kv.kviz_predmet = lecture
    if typ != "": kv.kviz_typ = typ

    kv.save()


def delete_otazka(request):    #req12

    otid = request.GET['otazka_id']
    print('delete otazka_id', otid)
    Otazka_def.objects.get(id = otid).delete()


def get_pokus_vysledok(request):    #req13

    pk_id = request.GET['pokus_id']

    pokus = Pokus.objects.get(id=pk_id)
    odpovede = Odpoved.objects.filter(pokus_id=pokus)
    print(odpovede)
    vysledky = {'pokus': [pokus.pokus_datum, pokus.pokus_zaciatok, pokus.pokus_koniec,
                          pokus.pokus_uhadol, pokus.pokus_neuhadol, pokus.pokus_neodpovedal,
                          pokus.pokus_body]}
    for i in range(0, len(odpovede)):
        otazka_def = Otazka_def.objects.get(id = odpovede[i].otazka_id).otazka_znenie  # FIXME zle vytvorena 'odpoved' je tam 'def' namiesto 'id'

        if odpovede[i].odpoved_moja == -1 :
            vysledky[i] = [otazka_def, "", -1, 0]
        else:
            mojaOdp = Odpoved_def.objects.get(id = odpovede[i].odpoved_moja)
            vysledky[i] = [otazka_def, mojaOdp.odpoved_znenie, mojaOdp.odpoved_spravna,
                           mojaOdp.odpoved_body]


    print(vysledky)
    return JsonResponse(vysledky)
