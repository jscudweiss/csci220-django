# Generated by Django 4.2.11 on 2024-04-21 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0017_auto_20240421_0433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonimage',
            name='image',
            field=models.ImageField(upload_to='media/pokeimages'),
        ),
    ]
