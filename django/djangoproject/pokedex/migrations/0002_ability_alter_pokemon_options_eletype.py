# Generated by Django 4.2.11 on 2024-04-11 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('abilityID', models.IntegerField(primary_key=True, serialize=False)),
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
                ('Effective', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokedex.eletype')),
            ],
        ),
    ]
