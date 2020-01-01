# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-01 16:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200101_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delicounter',
            name='cheese',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cheese', to='products.Product'),
        ),
        migrations.AlterField(
            model_name='delicounter',
            name='cured_meats',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cured_meats', to='products.Product'),
        ),
        migrations.AlterField(
            model_name='delicounter',
            name='fresh_meat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fresh_meat', to='products.Product'),
        ),
        migrations.AlterField(
            model_name='delicounter',
            name='fruit_veg',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fruit_veg', to='products.Product'),
        ),
    ]