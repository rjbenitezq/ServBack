# Generated by Django 2.0.4 on 2018-06-20 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TipoVehiculo', '0001_initial'),
        ('Cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehiculoCod', models.CharField(max_length=15, unique=True)),
                ('vehiculoPlaca', models.CharField(max_length=40, unique=True)),
                ('vehiculoMarca', models.CharField(max_length=20)),
                ('vehiculoModelo', models.CharField(max_length=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Cliente.Cliente')),
                ('tipoVehiculo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='TipoVehiculo.TipoVehiculo')),
            ],
        ),
    ]
