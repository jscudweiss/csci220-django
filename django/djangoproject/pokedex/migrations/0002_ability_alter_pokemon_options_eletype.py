# Generated by Django 4.2.11 on 2024-04-11 21:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('abilityID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('affect', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Abilities',
            },
        ),
        migrations.AlterModelOptions(
            name='pokemon',
            options={'verbose_name_plural': 'Pokemon'},
        ),
        migrations.CreateModel(
            name='EleType',
            fields=[
                ('Name', models.TextField(primary_key=True, serialize=False)),
                ('Effective', models.ManyToManyField(to='pokedex.eletype')),
                ('Pokemon', models.ManyToManyField(to='pokedex.pokemon')),
                ('Weakness', models.ManyToManyField(to='pokedex.eletype')),
            ],
        ),
    ]