# Generated by Django 2.0.6 on 2018-07-09 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Promocion', '0004_auto_20180707_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocion',
            name='motivo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Promocion.Motivo'),
        ),
    ]
