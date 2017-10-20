# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-02 12:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_search', '0002_auto_20170326_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]