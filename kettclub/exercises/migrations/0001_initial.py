# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-12 13:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import kettclub.exercises.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=2000, verbose_name='Description')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('creation_date', models.DateField(auto_now_add=True, null=True, verbose_name='Date')),
                ('language', models.IntegerField(verbose_name=1)),
                ('uuid', models.CharField(default=uuid.uuid4, editable=False, max_length=36, verbose_name='UUID')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ExerciseCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Exercise Categories',
            },
        ),
        migrations.CreateModel(
            name='ExerciseComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(help_text='A comment about how to correctly do this exercise.', max_length=200, verbose_name='Comment')),
                ('exercise', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='exercises.Exercise', verbose_name='Exercise')),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Only PNG and JPEG formats are supported', upload_to=kettclub.exercises.models.exercise_image_upload_dir, verbose_name='Image')),
                ('is_main', models.BooleanField(default=False, help_text='Tick the box if you want to set this image as the main one for the exercise (will be shown e.g. in the search). The first image is automatically marked by the system.', verbose_name='Main picture')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercises.Exercise', verbose_name='Exercise')),
            ],
            options={
                'ordering': ['-is_main', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Muscle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='In latin, e.g. "Pectoralis major"', max_length=50, verbose_name='Name')),
                ('is_front', models.BooleanField(default=1)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='exercise',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercises.ExerciseCategory', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='equipment',
            field=models.ManyToManyField(blank=True, to='exercises.Equipment', verbose_name='Equipment'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='muscles',
            field=models.ManyToManyField(blank=True, to='exercises.Muscle', verbose_name='Primary muscles'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='muscles_secondary',
            field=models.ManyToManyField(blank=True, related_name='secondary_muscles', to='exercises.Muscle', verbose_name='Secondary muscles'),
        ),
    ]
