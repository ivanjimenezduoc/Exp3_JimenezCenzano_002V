# Generated by Django 4.0.5 on 2022-06-22 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_categoria_vehiculo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiculo',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Vehiculo',
        ),
    ]
