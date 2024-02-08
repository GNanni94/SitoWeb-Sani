
from .models import Categoria
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


# Create your views here.

def card_categoria(request):
    lista_categorie = Categoria.objects.all()
    context = {
        'lista_categoria': lista_categorie,
    }
    template = loader.get_template('catalogo.html')
    return HttpResponse(template.render(context,request))

def categoria_home(request):
   return {
       'categoria': Categoria.objects.all()
   }


def dettaglio_categoria(request, categoria_id):
    return HttpResponse("Ciao")
