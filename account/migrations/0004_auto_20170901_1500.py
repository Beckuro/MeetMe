# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 15:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20170901_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinterest',
            name='interest',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='interestuser', to='account.Interest'),
        ),
    ]