from django.urls import path
from django.views.generic import TemplateView, CategoriaListView

urlpatterns = [
    path("catalogo", TemplateView.as_view(template_name="catalogo.html"), name = "catalogo"),
    path("categorie_home/", CategoriaListView.as_view(), name="dettaglio_categoria"),
]