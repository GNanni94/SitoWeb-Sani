# Generated by Django 4.1 on 2024-02-07 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prodotti', '0003_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='immagine_categortia',
            field=models.ImageField(default='logo/saniscope_logo 2.png', upload_to='immagini_categoria/'),
        ),
    ]
