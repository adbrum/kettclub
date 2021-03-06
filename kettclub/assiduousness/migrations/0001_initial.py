# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 00:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Presenca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('numeroatleta', models.IntegerField(verbose_name='Nº do Atleta')),
                ('datapresenca', models.DateField(blank=True, verbose_name='Data da presença')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
            ],
            options={
                'verbose_name': 'Presença',
                'verbose_name_plural': 'Presenças',
                'ordering': ('datapresenca',),
            },
        ),
    ]
