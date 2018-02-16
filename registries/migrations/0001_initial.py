# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-16 00:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gwells', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityCode',
            fields=[
                ('create_user', models.CharField(max_length=30)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(max_length=30, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('registries_activity_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('is_hidden', models.BooleanField(default=False)),
                ('display_order', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name_plural': 'Possible types of restricted activity, related to well drilling and pump installing',
                'db_table': 'registries_activity_code',
                'ordering': ['display_order', 'description'],
            },
        ),
        migrations.CreateModel(
            name='ApplicationStatusCode',
            fields=[
                ('create_user', models.CharField(max_length=30)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(max_length=30, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('registries_application_status_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('is_hidden', models.BooleanField(default=False)),
                ('display_order', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name_plural': 'Possible statuses of Applications',
                'db_table': 'registries_application_status_code',
                'ordering': ['display_order', 'description'],
            },
        ),
        migrations.CreateModel(
            name='ClassificationAppliedFor',
            fields=[
                ('create_user', models.CharField(max_length=30)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(max_length=30, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('classification_applied_for_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='UUID of the Registries Classification being applied for, hidden from users')),
                ('primary_certificate_no', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Registries Classification being applied for',
                'db_table': 'registries_classification_applied_for',
            },
        ),
        migrations.CreateModel(
            name='ContactAt',
            fields=[
                ('create_user', models.CharField(max_length=30)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(max_length=30, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('contact_at_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Contact At UUID, hidden from users')),
                ('contact_tel', models.CharField(blank=True, max_length=15, null=True, verbose_name='Contact telephone number')),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email adddress')),
                ('effective_date', models.DateField(default=datetime.date.today)),
                ('expired_date', models.DateField(blank=True, default=datetime.date.today, null=True)),
            ],
            options={
                'verbose_name_plural': 'Person contact details for a given Company',
                'db_table': 'registries_contact_at',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('create_user', models.CharField(max_length=30)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(max_length=30, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('org_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Organization UUID, hidden from users')),
                ('name', models.CharField(max_length=200)),
                ('street_address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Street Address')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='Town/City')),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='Postal Code')),
                ('main_tel', models.CharField(blank=True, max_length=15, null=True, verbose_name='Company main telephone number')),
                ('fax_tel', models.CharField(blank=True, max_length=15, null=True, verbose_name='Facsimile telephone number')),
                ('website_url', models.URLField(blank=True, null=True, verbose_name="Orgnization's Website")),
                ('certificate_authority', models.BooleanField(choices=[(False, 'No'), (True, 'Yes')], default=False, verbose_name='Certifying Authority for Registries Activities')),
                ('province_state', models.ForeignKey(db_column='province_state_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.ProvinceStateCode', verbose_name='Province/State')),
            ],
            options={
                'verbose_name_plural': 'Organizations',
                'db_table': 'registries_organization',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('create_user', models.CharField(max_length=30)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(max_length=30, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('person_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Person UUID, hidden from users')),
                ('first_name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Persons',
                'db_table': 'registries_person',
                'ordering': ['first_name', 'surname'],
            },
        ),
        migrations.CreateModel(
            name='QualificationCode',
            fields=[
                ('create_user', models.CharField(max_length=30)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(max_length=30, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('registries_qualification_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=100)),
                ('is_hidden', models.BooleanField(default=False)),
                ('display_order', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name_plural': 'Possible qualifications, under a given Activity and Subactivity',
                'db_table': 'registries_qualification_code',
                'ordering': ['display_order', 'description'],
            },
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('create_user', models.CharField(max_length=30)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(max_length=30, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('register_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Register UUID, hidden from users')),
                ('registration_no', models.CharField(blank=True, max_length=15, null=True)),
                ('registration_date', models.DateField(blank=True, null=True)),
                ('register_removal_date', models.DateField(blank=True, null=True, verbose_name='Date of Removal from Register')),
            ],
            options={
                'verbose_name_plural': 'Register of Drillers and Pump Installers',
                'db_table': 'registries_register',
            },
        ),
        migrations.CreateModel(
            name='RegistriesApplication',
            fields=[
                ('create_user', models.CharField(max_length=30)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(max_length=30, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('application_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Register Application UUID, hidden from users')),
                ('file_no', models.CharField(blank=True, max_length=25, null=True, verbose_name='ORCS File # reference.')),
                ('over19_ind', models.BooleanField(default=True)),
                ('registrar_notes', models.CharField(blank=True, max_length=255, null=True, verbose_name='Registrar Notes, for internal use only.')),
                ('reason_denied', models.CharField(blank=True, max_length=255, null=True, verbose_name='Free form text explaining reason for denial.')),
                ('person', models.ForeignKey(db_column='person_guid', on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='registries.Person', verbose_name='Person Reference')),
            ],
            options={
                'verbose_name_plural': 'Applications for Driller or Pump Installer',
                'db_table': 'registries_application',
            },
        ),
        migrations.CreateModel(
            name='RegistriesApplicationStatus',
            fields=[
                ('create_user', models.CharField(max_length=30)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(max_length=30, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('application_status_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Register Application Status UUID, hidden from users')),
                ('notified_date', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('effective_date', models.DateField(default=datetime.date.today)),
                ('expired_date', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('application', models.ForeignKey(db_column='application_guid', on_delete=django.db.models.deletion.CASCADE, to='registries.RegistriesApplication', verbose_name='Application Reference')),
                ('status', models.ForeignKey(db_column='registries_application_status_guid', on_delete=django.db.models.deletion.CASCADE, to='registries.ApplicationStatusCode', verbose_name='Application Status Code Reference')),
            ],
            options={
                'verbose_name_plural': 'Status for a given Application',
                'db_table': 'registries_application_status',
                'ordering': ['application', 'effective_date'],
            },
        ),
        migrations.CreateModel(
            name='RegistriesRemovalReason',
            fields=[
                ('create_user', models.CharField(max_length=30)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(max_length=30, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('registries_removal_reason_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('is_hidden', models.BooleanField(default=False)),
                ('display_order', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name_plural': 'Possible reasons for removal from either of the Registers',
                'db_table': 'registries_removal_reason_code',
                'ordering': ['display_order', 'description'],
            },
        ),
        migrations.CreateModel(
            name='RegistriesStatusCode',
            fields=[
                ('create_user', models.CharField(max_length=30)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(max_length=30, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('registries_status_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('is_hidden', models.BooleanField(default=False)),
                ('display_order', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name_plural': 'Possible Status Codes of Register Entries',
                'db_table': 'registries_status_code',
                'ordering': ['display_order', 'description'],
            },
        ),
        migrations.CreateModel(
            name='SubactivityCode',
            fields=[
                ('create_user', models.CharField(max_length=30)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(max_length=30, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('registries_subactivity_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=100)),
                ('is_hidden', models.BooleanField(default=False)),
                ('display_order', models.PositiveIntegerField()),
                ('registries_activity', models.ForeignKey(blank=True, db_column='registries_activity_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='registries.ActivityCode')),
            ],
            options={
                'verbose_name_plural': 'Possible subtypes of restricted activity, under a given Activity',
                'db_table': 'registries_subactivity_code',
                'ordering': ['display_order', 'description'],
            },
        ),
        migrations.AddField(
            model_name='register',
            name='register_removal_reason',
            field=models.ForeignKey(blank=True, db_column='registries_removal_reason_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='registries.RegistriesRemovalReason', verbose_name='Removal Reason'),
        ),
        migrations.AddField(
            model_name='register',
            name='registries_activity',
            field=models.ForeignKey(blank=True, db_column='registries_activity_guid', on_delete=django.db.models.deletion.CASCADE, to='registries.ActivityCode'),
        ),
        migrations.AddField(
            model_name='register',
            name='registries_application',
            field=models.ForeignKey(blank=True, db_column='application_guid', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to='registries.RegistriesApplication', verbose_name='Application Reference'),
        ),
        migrations.AddField(
            model_name='register',
            name='status',
            field=models.ForeignKey(db_column='registries_status_guid', on_delete=django.db.models.deletion.CASCADE, to='registries.RegistriesStatusCode', verbose_name='Register Entry Status'),
        ),
        migrations.AddField(
            model_name='qualificationcode',
            name='registries_subactivity',
            field=models.ForeignKey(blank=True, db_column='registries_subactivity_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='registries.SubactivityCode'),
        ),
        migrations.AddField(
            model_name='contactat',
            name='org',
            field=models.ForeignKey(db_column='org_guid', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='registries.Organization', verbose_name='Company Reference'),
        ),
        migrations.AddField(
            model_name='contactat',
            name='person',
            field=models.ForeignKey(db_column='person_guid', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='companies', to='registries.Person', verbose_name='Person Reference'),
        ),
        migrations.AddField(
            model_name='classificationappliedfor',
            name='primary_certificate_authority',
            field=models.ForeignKey(db_column='certifying_org_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='registries.Organization', verbose_name='Certifying Organization'),
        ),
        migrations.AddField(
            model_name='classificationappliedfor',
            name='registries_application',
            field=models.ForeignKey(db_column='application_guid', on_delete=django.db.models.deletion.CASCADE, to='registries.RegistriesApplication', verbose_name='Application Reference'),
        ),
        migrations.AddField(
            model_name='classificationappliedfor',
            name='registries_subactivity',
            field=models.ForeignKey(db_column='registries_subactivity_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='registries.SubactivityCode'),
        ),
    ]
