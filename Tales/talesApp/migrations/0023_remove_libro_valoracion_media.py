# Generated by Django 5.0.6 on 2024-06-06 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('talesApp', '0022_remove_retos_descripcion_reto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='valoracion_media',
        ),
    ]
