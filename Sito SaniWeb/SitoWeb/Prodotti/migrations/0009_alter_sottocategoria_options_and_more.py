# Generated by Django 4.1 on 2024-02-07 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Prodotti', '0008_sottocategoria_remove_categoria_sottocategoria_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sottocategoria',
            options={'verbose_name': 'Sottocategoria', 'verbose_name_plural': 'Sottocategoria'},
        ),
        migrations.AlterModelTable(
            name='sottocategoria',
            table='Sottocategoria',
        ),
    ]
