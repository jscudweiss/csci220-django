# Generated by Django 4.2.11 on 2024-04-05 01:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('minifacebook', '0003_poke'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]