# Generated by Django 4.1 on 2024-02-07 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Prodotti', '0006_alter_categoria_options_alter_articolo_id_categoria_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='sottocategoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Prodotti.categoria'),
        ),
    ]