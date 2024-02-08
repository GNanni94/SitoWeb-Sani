from django.db.models import Q
from django.shortcuts import render
from .models import Categoria
from django.views.generic import ListView, DetailView
from typing import Any, Dict
from django.http import HttpRequest, HttpResponse

# Create your views here.


class CategoriaListView(ListView):
    model=Categoria
    template_name = "home.html"


def categorie(request):
    return {
        'categoria': Categoria.objects.all()
    }
