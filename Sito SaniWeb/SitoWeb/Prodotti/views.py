
from .models import Categoria
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import TemplateView



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


def dettaglio_categoria(request, categoria_nome):
    if categoria_nome.casefold() == "prodotti chimici":
        template = loader.get_template('prodotti_tabella.html')
        context= {
            'nome_categoria': categoria_nome
        }   
        return HttpResponse(template.render(context, request))
    template = loader.get_template('prodotti_card.html')   
    context= {
        'nome_categoria': categoria_nome
    }     
    return HttpResponse(template.render(context, request))

    
