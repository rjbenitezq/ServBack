# Generated by Django 2.0.4 on 2018-06-20 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Juridico', '0001_initial'),
        ('Persona', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clienteCod', models.CharField(max_length=15, unique=True)),
                ('clienteAbrev', models.CharField(max_length=1)),
                ('juridico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Juridico.Juridico')),
                ('persona', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Persona.Persona')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]