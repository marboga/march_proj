# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-23 23:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='locations_spoken',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spoken_languages', to='theme_app.Location'),
        ),
    ]
