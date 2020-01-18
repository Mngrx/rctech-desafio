from django.shortcuts import render
from .models import Noticia


# Create your views here.

def noticias_listar(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticias/listar.html', {'noticias': noticias})