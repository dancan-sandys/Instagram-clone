# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-19 16:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myInstagram', '0007_auto_20201019_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='photo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myInstagram.Photo'),
            preserve_default=False,
        ),
    ]
