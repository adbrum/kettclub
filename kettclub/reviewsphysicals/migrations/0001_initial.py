# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-03 19:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subscriptions', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataavaliacao', models.DateField(verbose_name='Data da avaliação')),
                ('peso', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Peso Kg')),
                ('metbasal', models.CharField(max_length=5, verbose_name='Met. basal Kcal')),
                ('idadebiologica', models.IntegerField(verbose_name='Idade biológica anos')),
                ('agua', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Água %')),
                ('gorduraviceral', models.CharField(max_length=5, verbose_name='Gordura visceral nível')),
                ('massaossea', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Massa ossea kg')),
                ('massamuscular', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Massa muscular total kg')),
                ('massagorda', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Massa gorda total %')),
                ('pescoco', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Pescoço cm')),
                ('ombros', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Ombros cm')),
                ('peitos', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Peitos cm')),
                ('cintura', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Cintura cm')),
                ('abdominal', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Abdominal cm')),
                ('quadril', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Quadril cm')),
                ('coxaproximal', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Coxa proximal cm')),
                ('coxamedial', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Coxa medial cm')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Avaliado em')),
                ('atleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscriptions.Subscription', verbose_name='Nº do atleta')),
            ],
            options={
                'verbose_name': 'Avaliação',
                'ordering': ('atleta__nome',),
                'verbose_name_plural': 'Avaliações',
            },
        ),
    ]
