# Generated by Django 2.0.7 on 2018-07-23 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Juridico', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juridico',
            name='juridicoCod',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='juridico',
            name='juridicoEmail',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='juridico',
            name='juridicoRUC',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='juridico',
            name='juridicoRazonSocial',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
