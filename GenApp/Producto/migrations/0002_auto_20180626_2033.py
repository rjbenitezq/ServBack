# Generated by Django 2.0.6 on 2018-06-27 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='combustible',
            name='combustibleEstado',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='producto',
            name='productoEstado',
            field=models.CharField(max_length=1),
        ),
    ]
