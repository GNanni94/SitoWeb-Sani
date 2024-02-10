
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
        return "Id: "+ str(self.pk)+",   codice articolo: " + self.codiece_articolo + ",   nome articolo: " + self.nome_articolo

    class Meta:
        db_table="Articoli"
        verbose_name = "Articolo"
        verbose_name_plural ="Articoli"


class Categoria(models.Model):
    nome_categoria=models.CharField(max_length=30, blank=True)
    immagine_categoria = models.ImageField(upload_to='immagini_categoria/', default ="logo/saniscope_logo 2.png")
    

    def __str__ (self):
        return "Id: "+ str(self.pk) +",  nome categoria: " + self.nome_categoria 

   
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

class ImmaginiAritcolo(models.Model):
    immagine_articolo = models.ImageField(upload_to='immagini_articoli/', default ="logo/saniscope_logo 2.png")
    id_articolo =models.ForeignKey(Articolo, on_delete=models.CASCADE, blank=True)


    def __str__ (self):
        return "Id: "+ str(self.pk) +",  nome articolo: " + self.id_articolo.nome_articolo

    class Meta:
        db_table="ImmaginiAritcolo"
        verbose_name = "ImmaginiAritcolo"
        verbose_name_plural ="ImmaginiAritcolo"


class SchedeTecniche (models.Model):
    data_inizio = models.DateTimeField(auto_now_add=True)
    data_fine= models.DateTimeField( blank = True)
    scheda = models.FileField(upload_to ="schede_tecniche/", blank=True)
    id_articolo = models.OneToOneField(Articolo,on_delete=models.CASCADE, blank=True, parent_link = False)

    class Meta:
        db_table="SchedeTecniche"
        verbose_name = "SchedeTecniche"
        verbose_name_plural ="SchedeTecniche"