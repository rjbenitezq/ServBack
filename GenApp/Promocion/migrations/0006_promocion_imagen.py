# Generated by Django 2.0.7 on 2018-07-16 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Promocion', '0005_auto_20180709_0235'),
    ]

    operations = [
        migrations.AddField(
            model_name='promocion',
            name='imagen',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
