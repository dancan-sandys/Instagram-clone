# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-20 06:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myInstagram', '0008_comments_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
