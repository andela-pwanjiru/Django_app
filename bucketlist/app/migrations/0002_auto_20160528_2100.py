# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-28 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='password_two',
            field=models.CharField(max_length=255),
        ),
    ]
