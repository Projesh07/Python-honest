# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-08 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0015_auto_20180207_0651'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='is_highlighted',
            field=models.IntegerField(default=0),
        ),
    ]