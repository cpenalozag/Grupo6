# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 22:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alerta',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='id')),
            ],
        ),
        migrations.CreateModel(
            name='Rango',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('valorMin', models.BigIntegerField(verbose_name='valorMin')),
                ('valorMax', models.BigIntegerField(verbose_name='valorMax')),
            ],
        ),
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.TimeField(verbose_name='dia')),
                ('anotaciones', models.CharField(max_length=1000, verbose_name='anotaciones')),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('time', models.TimeField(verbose_name='time')),
                ('valor', models.IntegerField(verbose_name='valor')),
                ('estado', models.CharField(max_length=1, verbose_name='estado')),
            ],
        ),
        migrations.CreateModel(
            name='SubReporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valMinimo', models.DecimalField(decimal_places=3, max_digits=7)),
                ('valMaximo', models.DecimalField(decimal_places=3, max_digits=7)),
                ('valPromedio', models.DecimalField(decimal_places=3, max_digits=7)),
                ('variacion', models.DecimalField(decimal_places=3, max_digits=7)),
                ('sensor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Sensor')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('nombre', models.CharField(max_length=23, verbose_name='nombre tipo')),
            ],
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('zona', models.IntegerField(verbose_name='zona')),
                ('area', models.IntegerField(verbose_name='area')),
                ('nivel', models.IntegerField(verbose_name='nivel')),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=64, unique=True, verbose_name='usuario')),
                ('rol', models.CharField(max_length=1, verbose_name='rol')),
                ('contrasena', models.CharField(max_length=128, verbose_name='contraseña')),
                ('access_token', models.CharField(max_length=256, verbose_name='access_token')),
                ('reportes', models.ManyToManyField(to='dashboard.Reporte')),
            ],
        ),
        migrations.AddField(
            model_name='sensor',
            name='tipo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='tipo', to='dashboard.Tipo'),
        ),
        migrations.AddField(
            model_name='sensor',
            name='ubicacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Ubicacion'),
        ),
    ]
