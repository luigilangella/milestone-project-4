# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-28 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20200128_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
