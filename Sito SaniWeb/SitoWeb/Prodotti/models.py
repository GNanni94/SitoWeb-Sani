from django.db import models
from django.urls import reverse

# Create your models here.

class Articolo(models.Model):
    UNITA_MISURA=(
        ('kg', 'Kilogrammo'),
        ('Lt','Litro'),
        ('Nr','Numero'),
    )
    codiece_articolo=models.CharField(max_length=7, unique=True, blank=True)
    nome_articolo=models.CharField(max_length=30,blank=True)
    descrizione=models.CharField(max_length=250, blank=True)
    unita_di_misura = models.CharField(max_length=2, choices=UNITA_MISURA)
    id_categoria=models.ForeignKey("Categoria", on_delete=models.CASCADE, blank=True, null=True)

    def __str__ (self):
        return str(self.pk)+" " + self.nome_articolo + " " + self.codiece_articolo

    class Meta:
        db_table="Articoli"
        verbose_name = "Articolo"
        verbose_name_plural ="Articoli"


class Categoria(models.Model):
    nome_categoria=models.CharField(max_length=30, blank=True)
    immagine_categortia = models.ImageField(upload_to='immagini_categoria/', default ="logo/saniscope_logo 2.png")
    

    def __str__ (self):
        return self.immagine_categortia.url + " "+str(self.pk) +" " + self.nome_categoria 

   
    class Meta:
        db_table="Categoria"
        verbose_name = "Categoria"
        verbose_name_plural ="Categoria"

    
class Sottocategoria(models.Model):
    nome_sottocategoria=models.CharField(max_length=30, blank=True)
    gruppo=models.IntegerField()
    id_categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE, blank=True, null=True)

    def __str__ (self):
        return str(self.pk) +" " + self.nome_sottocategoria 
    
    class Meta:
        db_table="Sottocategoria"
        verbose_name = "Sottocategoria"
        verbose_name_plural ="Sottocategoria"