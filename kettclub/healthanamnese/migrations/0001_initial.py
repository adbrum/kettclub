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
            name='SaudeAnamnese',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quest01', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], verbose_name='Doença cardiovascular ou pulmonar (asma, bronquite, etc.)')),
                ('quest02', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], verbose_name='Doença metabólica (tiroide, renal ou hepática)')),
                ('quest03', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], verbose_name='Diabetes tipo I ou II')),
                ('quest04', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], verbose_name='Dor ou desconforto no peito em repouso ou exercício')),
                ('quest05', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], verbose_name='Desmaios, tonturas ou perda de consciência')),
                ('quest06', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], verbose_name='Dificuldades em respirar ou problemas respiratórios repentinos durante a noite')),
                ('quest07', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], verbose_name='Palpitações ou taquicardia')),
                ('quest08', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], verbose_name='Dor severa nas pernas durante a marcha')),
                ('quest09', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], verbose_name='Tensão arterial maior que 140/90 mm Hg ou sob medicação')),
                ('quest010', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], verbose_name='Edema no tornozelo')),
                ('quest011', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], verbose_name='Colesterol Total maior que 240 mg/dl ou sob medicação')),
                ('quest012', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], verbose_name='História familiar de enfarte do miocárdio ou morte súbita do pai/mãe ou outro familiar em primeiro grau antes dos 55/65 anos')),
                ('quest013', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], verbose_name='Índice de Massa Corporal maior que 30 (kg/m2)')),
                ('quest014', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], verbose_name='Fumador ou que tenha deixado de fumar nos últimos 6 meses')),
                ('quest015', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], verbose_name='Sem programa de exercício regular há mais de 6 meses')),
                ('quest016', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], verbose_name='Algum problema de saúde não mencionado e/ou qualquer outro fator condicionante do programa de exercício físico a elaborar?')),
                ('quest017', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], verbose_name='Doença recente?')),
                ('quest018', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], verbose_name='Hospitalização?')),
                ('quest019', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], verbose_name='Procedimentos cirúrgicos?')),
                ('quest020', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], verbose_name='Pratica algum tipo de exercício regularmente fora do KC?')),
                ('quest021', models.TextField(blank=True, verbose_name='Se sim, qual e quantas vezes por semana?')),
                ('quest022', models.TextField(blank=True, verbose_name='Alguma observação importante a declarar?')),
                ('quest023', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], verbose_name='Declara que compreendeu integralmente o conteúdo deste documento?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atleta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='subscriptions.Atleta', verbose_name='Nº do atleta')),
            ],
            options={
                'verbose_name': 'Questionário de Saúde e Anamnese Desportiva',
                'verbose_name_plural': 'Questionário de Saúde e Anamnese Desportiva',
            },
        ),
    ]
