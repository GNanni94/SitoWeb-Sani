from django.urls import path
from django.views.generic import TemplateView
from .views import card_categoria, dettaglio_categoria

urlpatterns = [
    path("", card_categoria, name = "catalogo"),
    path("<int:categoria_id>/", dettaglio_categoria, name="dettaglio_categoria"),
]