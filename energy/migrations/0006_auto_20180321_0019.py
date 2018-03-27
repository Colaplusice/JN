# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-20 16:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0005_auto_20180319_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='message',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='energy.Type', to_field='name'),
        ),
    ]
