from django.shortcuts import render
from .models import Noticia
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.http import HttpResponse


# Create your views here.

def noticias_listar(request):
    noticias = Noticia.objects.all()
    # noticias = serializers.serialize('json', Noticia.objects.all())
    return render(request, 'noticias/listar.html', {'noticias': noticias})
