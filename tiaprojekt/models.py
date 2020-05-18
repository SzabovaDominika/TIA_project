from django.db import models
from django.contrib.auth.models import User


# each class has its private key behind the scenes
# to reach PK, just type <element name>.id or .pk

# after each change, need to run in terminal
# 'python manage.py makemigrations tiaprojekt'
# 'python manage.py migrate'

# ak by sme chceli vypisat objekty prvky tabulky nejak pekne, tak
# napiseme def __str__(self): return self.<>+' '+....

# modules relation FK https://docs.djangoproject.com/en/3.0/ref/models/relations/
# FK = <class name>.objects.get(id=<id>)
# element.id = FK

class Kviz_def(models.Model):
    user = models.IntegerField(default=-1)
    kviz_nazov = models.CharField(max_length=50)
    kviz_predmet = models.CharField(max_length=100)
    kviz_typ = models.CharField(max_length=50)
    kviz_vytvoreny = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.id) + ' = ' + self.kviz_nazov


class Otazka_def(models.Model):
    kviz_id = models.ForeignKey(Kviz_def, on_delete=models.CASCADE)
    otazka_znenie = models.TextField(null=False, blank=False, default="-")

    def __str__(self):
        return str(self.id) + ' = ' + self.otazka_znenie


class Odpoved_def(models.Model):
    otazka_id = models.ForeignKey(Otazka_def, on_delete=models.CASCADE)
    odpoved_znenie = models.TextField(null=True, blank=True)
    odpoved_body = models.IntegerField()
    odpoved_spravna = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + ' = ' + self.odpoved_znenie + '-' + str(
            self.odpoved_body) + '-' + str(self.odpoved_spravna)


class Pokus(models.Model):
    user = models.IntegerField(default=-1)
    kviz_id = models.ForeignKey(Kviz_def, on_delete=models.CASCADE)
    pokus_datum = models.DateField(auto_now=True)
    pokus_zaciatok = models.TimeField(auto_now=True)
    pokus_koniec = models.TimeField(auto_now=True)
    pokus_uhadol = models.IntegerField()
    pokus_neuhadol = models.IntegerField()
    pokus_neodpovedal = models.IntegerField()
    pokus_body_zisk = models.IntegerField(default=0)
    pokus_body_max = models.IntegerField(default=0)

    def duration(self):
        return self.pokus_koniec - self.pokus_zaciatok

    def __str__(self):
        return str(self.id) + ' = ' + str(self.pokus_datum) + '/' + str(self.pokus_body)


class Odpoved(models.Model):
    pokus_id = models.ForeignKey(Pokus, on_delete=models.CASCADE, default=0)
    otazka_id = models.IntegerField()
    odpoved_moja = models.IntegerField(default=-1)


class Links(models.Model):
    user = models.IntegerField(default=-1)
    link = models.TextField(null=True, blank=True)
    show_as = models.TextField(null=True, blank=True)
