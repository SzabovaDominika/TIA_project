from django.db import models

 # each class has its private key behind the scenes
 # to reach PK, just type <element name>.id or .pk

 # after each change, need to run
 # 'python manage.py makemigrations tiaprojekt'

# ak by sme chceli vypisat objekty prvky tabulky nejak pekne, tak
#napiseme def __str__(self): return self.<>+' '+....

# modules relation FK https://docs.djangoproject.com/en/3.0/ref/models/relations/
# FK = <class name>.objects.get(id=<id>)
# element.id = FK


class Kviz_def(models.Model):
    kviz_nazov = models.CharField(max_length=50)
    kviz_predmet = models.CharField(max_length=100)
    kviz_typ = models.CharField(max_length=20)
    kviz_vytvoreny = models.DateField(auto_now=True)

class Otazka_def(models.Model):
    kviz_id = models.ForeignKey(Kviz_def, on_delete=models.DO_NOTHING)
    otazka_znenie = models.TextField(null=False, blank=False, default="-")

    def __str__(self):
        return self.otazka_znenie

class Odpoved_def(models.Model):
    otazka_id = models.ForeignKey(Otazka_def, on_delete=models.DO_NOTHING)
    odpoved_znenie = models.TextField(null=True, blank=True)
    odpoved_body = models.IntegerField()
    odpoved_spravna = models.BooleanField(default=False)

    def __str__(self):
        return self.odpoved_znenie+'-'+str(self.odpoved_body)+'-'+str(self.odpoved_spravna)

class Pokus(models.Model):
    kviz_id = models.ForeignKey(Kviz_def, on_delete=models.DO_NOTHING)
    pokus_datum = models.DateField(auto_now=True)
    pokus_zaciatok = models.TimeField(auto_now=True)
    pokus_koniec = models.TimeField(auto_now=True)
    pokus_uhadol = models.IntegerField()
    pokus_neuhadol = models.IntegerField()
    pokus_neodpovedal = models.IntegerField()
    pokus_body = models.IntegerField(default=0)

    def duration(self):
        return self.pokus_koniec-self.pokus_zaciatok
class Odpoved(models.Model):
    pokus_id = models.ForeignKey(Pokus, on_delete=models.DO_NOTHING, default=0)
    otazka_id = models.ForeignKey(Otazka_def, on_delete=models.DO_NOTHING)
    odpoved_moja = models.ForeignKey(Odpoved_def, on_delete=models.DO_NOTHING)


class Skusanie(models.Model):
    termin = models.DateField(auto_now=True)
    popis = models.TextField(null=True, blank=True, default="-")