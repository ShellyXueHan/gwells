# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-02-02 23:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registries', '0002_auto_20180201_0618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classificationappliedfor',
            name='primary_certificate_authority',
            field=models.ForeignKey(db_column='certifying_org_guid', on_delete=django.db.models.deletion.CASCADE, to='registries.Organization', verbose_name='Certifying Organization'),
        ),
    ]