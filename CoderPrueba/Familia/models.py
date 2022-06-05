from django.db import models

# Create your models here.

class Padres(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()

class Hermanos(models.Model):
    nombre = models.CharField(max_length=30)
    profesion = models.CharField(max_length=30)
    cumpleaños = models.DateField()
    estadoCivil = models.CharField(max_length=20)

class Tios(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
