# Generated by Django 2.0.6 on 2018-06-26 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Promocion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='motivo',
            name='motivoTipo',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]