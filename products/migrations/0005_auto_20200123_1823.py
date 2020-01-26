# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-23 18:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200123_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogcategory',
            name='catalog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='products.Catalog'),
        ),
        migrations.AlterField(
            model_name='catalogcategory',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.CatalogCategory'),
        ),
    ]
