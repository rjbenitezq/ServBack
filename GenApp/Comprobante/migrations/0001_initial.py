# Generated by Django 2.0.4 on 2018-06-20 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cliente', '0001_initial'),
        ('Sucursal', '0001_initial'),
        ('Promocion', '0001_initial'),
        ('Producto', '0001_initial'),
        ('Trabajador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comprobante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comprobanteCod', models.CharField(max_length=15, unique=True)),
                ('combrobanteCantidad', models.FloatField()),
                ('comprobanteTotal', models.FloatField()),
                ('comprobanteFecha', models.DateTimeField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Cliente.Cliente')),
                ('combustible', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='Producto.Combustible')),
                ('producto', models.ManyToManyField(blank=True, to='Producto.Producto')),
                ('promocion', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='Promocion.Promocion')),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Sucursal.Sucursal')),
                ('trabajador', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Trabajador.Trabajador')),
            ],
        ),
    ]
