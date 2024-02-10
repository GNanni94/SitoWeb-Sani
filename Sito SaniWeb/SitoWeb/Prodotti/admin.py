from django.contrib import admin
from .models import Articolo, Categoria, Sottocategoria, ImmaginiAritcolo, SchedeTecniche

# Register your models here.

admin.site.register(Articolo)
admin.site.register(Categoria)
admin.site.register(Sottocategoria)
admin.site.register(ImmaginiAritcolo)
admin.site.register(SchedeTecniche)