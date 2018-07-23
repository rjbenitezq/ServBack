# Generated by Django 2.0.4 on 2018-06-20 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Area', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargoCod', models.CharField(max_length=20, unique=True)),
                ('cargoDescripcion', models.CharField(max_length=80)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Area.Area')),
            ],
        ),
    ]
