# Generated by Django 2.0.6 on 2018-06-21 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sucursal', '0001_initial'),
        ('Area', '0002_auto_20180620_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='sucursal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Sucursal.Sucursal'),
        ),
    ]
