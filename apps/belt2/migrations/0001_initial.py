# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 02:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poke',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('alias', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=100)),
                ('birth_date', models.DateTimeField()),
                ('password', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='poke',
            name='pokee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poked', to='belt2.User'),
        ),
        migrations.AddField(
            model_name='poke',
            name='poker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poked_by', to='belt2.User'),
        ),
    ]
