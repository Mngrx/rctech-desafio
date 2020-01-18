from django.db import models
from django.utils import timezone


# Create your models here.


class Site(models.Model):
    nome = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    data_ins = models.DateTimeField(default=timezone.now)


class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    texto = models.TextField()
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    data_ins = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo
