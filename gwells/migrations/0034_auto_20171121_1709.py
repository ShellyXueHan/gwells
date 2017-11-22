# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-21 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gwells', '0033_auto_20171120_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='well',
            name='alternative_specs_submitted',
            field=models.BooleanField(choices=[(False, 'No'), (True, 'Yes')], default=False, verbose_name='Alternative specs submitted (if required)'),
        ),
    ]