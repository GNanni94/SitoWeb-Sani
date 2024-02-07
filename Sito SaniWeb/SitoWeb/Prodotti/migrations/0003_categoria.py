# Generated by Django 4.1 on 2024-02-07 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prodotti', '0002_alter_articolo_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_categoria', models.CharField(blank=True, max_length=30)),
                ('immagine_categortia', models.ImageField(default='media/logo/saniscope_logo 2.png', upload_to='media/immagini_categoria/')),
            ],
        ),
    ]
