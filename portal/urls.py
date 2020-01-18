from django.urls import path
from . import views


urlpatterns = [
    path('', views.noticias_listar, name='noticias_listar'),
]