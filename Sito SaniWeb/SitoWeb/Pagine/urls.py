from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name = "home"),
    path("home", TemplateView.as_view(template_name="home.html"), name = "home"),
    path("Storia Azienda", TemplateView.as_view(template_name="storia_azienda.html"), name = "storia_azienda"),
    path("etichettatura ambientale",TemplateView.as_view(template_name="etichettatura_ambientale.html"), name = "etichettatura_ambientale"),
    path("condizioniDiVendita", TemplateView.as_view(template_name="condizioni_vendita.html"), name = "condizioni_vendita"),
    path("politicheAziendali", TemplateView.as_view(template_name="politiche_aziendali.html"), name = "politiche_aziendali"),
    path("contatti", TemplateView.as_view(template_name="contatti.html"), name = "contatti"),

]