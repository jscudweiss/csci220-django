# Generated by Django 4.2.11 on 2024-04-21 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0018_alter_pokemonimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonimage',
            name='image',
            field=models.ImageField(upload_to='pokeimages'),
        ),
    ]
