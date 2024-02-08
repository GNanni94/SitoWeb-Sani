
from .models import Categoria
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


# Create your views here.



def categoria_home(request):
   return {
       'categoria': Categoria.objects.all()
   }
