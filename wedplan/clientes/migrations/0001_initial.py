# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=10, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('face', models.URLField(blank=True, max_length=500, null=True, unique=True)),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
    ]
