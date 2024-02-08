from django.urls import path
from django.views.generic import TemplateView
from .views import categoria_home

urlpatterns = [
    path("", TemplateView.as_view(template_name="catalogo.html"), name = "catalogo"),
    path("lista_categoria", categoria_home, name='categoria_home'),
]