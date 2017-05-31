# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-30 23:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gwells', '0018_auto_20170529_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivitySubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('driller_name', models.CharField(blank=True, max_length=200, verbose_name='Name of Person Who Did the Work')),
                ('consultant_name', models.CharField(blank=True, max_length=200, verbose_name='Consultant Name')),
                ('consultant_company', models.CharField(blank=True, max_length=200, verbose_name='Consultant Company')),
                ('work_start_date', models.DateField(verbose_name='Work Start Date')),
                ('work_end_date', models.DateField(verbose_name='Work End Date')),
                ('owner_full_name', models.CharField(max_length=200, verbose_name='Owner Name')),
                ('owner_mailing_address', models.CharField(max_length=100, verbose_name='Mailing Address')),
                ('owner_city', models.CharField(max_length=100, verbose_name='Town/City')),
                ('owner_postal_code', models.CharField(blank=True, max_length=10, verbose_name='Postal Code')),
                ('street_address', models.CharField(blank=True, max_length=100, verbose_name='Street Address')),
                ('city', models.CharField(blank=True, max_length=50, verbose_name='Town/City')),
                ('legal_lot', models.CharField(blank=True, max_length=10, verbose_name='Lot')),
                ('legal_plan', models.CharField(blank=True, max_length=20, verbose_name='Plan')),
                ('legal_district_lot', models.CharField(blank=True, max_length=20, verbose_name='District Lot')),
                ('legal_block', models.CharField(blank=True, max_length=10, verbose_name='Block')),
                ('legal_section', models.CharField(blank=True, max_length=10, verbose_name='Section')),
                ('legal_township', models.CharField(blank=True, max_length=20, verbose_name='Township')),
                ('legal_range', models.CharField(blank=True, max_length=10, verbose_name='Range')),
                ('legal_pid', models.PositiveIntegerField(blank=True, null=True, verbose_name='PID')),
                ('well_location_description', models.CharField(blank=True, max_length=500, verbose_name='Well Location Description')),
                ('identification_plate_number', models.PositiveIntegerField(blank=True, null=True, unique=True)),
                ('well_tag_number', models.PositiveIntegerField(blank=True, null=True, unique=True)),
                ('diameter', models.CharField(blank=True, max_length=9)),
                ('total_depth_drilled', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('finished_well_depth', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('well_yield', models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True)),
                ('driller_responsible', models.ForeignKey(db_column='gwells_driller_responsible_id', on_delete=django.db.models.deletion.CASCADE, to='gwells.Driller', verbose_name='Person Responsible for Drilling')),
            ],
            options={
                'db_table': 'gwells_activity_submission',
            },
        ),
        migrations.CreateModel(
            name='LtsaOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('full_name', models.CharField(max_length=200, verbose_name='Owner Name')),
                ('mailing_address', models.CharField(max_length=100, verbose_name='Mailing Address')),
                ('city', models.CharField(max_length=100, verbose_name='Town/City')),
                ('postal_code', models.CharField(blank=True, max_length=10, verbose_name='Postal Code')),
                ('province_state', models.ForeignKey(blank=True, db_column='gwells_province_state_id', on_delete=django.db.models.deletion.CASCADE, to='gwells.ProvinceState', verbose_name='Province')),
            ],
            options={
                'db_table': 'gwells_ltsa_owner',
            },
        ),
        migrations.CreateModel(
            name='Well',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('owner_full_name', models.CharField(max_length=200, verbose_name='Owner Name')),
                ('owner_mailing_address', models.CharField(max_length=100, verbose_name='Mailing Address')),
                ('owner_city', models.CharField(max_length=100, verbose_name='Town/City')),
                ('owner_postal_code', models.CharField(blank=True, max_length=10, verbose_name='Postal Code')),
                ('street_address', models.CharField(blank=True, max_length=100, verbose_name='Street Address')),
                ('city', models.CharField(blank=True, max_length=50, verbose_name='Town/City')),
                ('legal_lot', models.CharField(blank=True, max_length=10, verbose_name='Lot')),
                ('legal_plan', models.CharField(blank=True, max_length=20, verbose_name='Plan')),
                ('legal_district_lot', models.CharField(blank=True, max_length=20, verbose_name='District Lot')),
                ('legal_block', models.CharField(blank=True, max_length=10, verbose_name='Block')),
                ('legal_section', models.CharField(blank=True, max_length=10, verbose_name='Section')),
                ('legal_township', models.CharField(blank=True, max_length=20, verbose_name='Township')),
                ('legal_range', models.CharField(blank=True, max_length=10, verbose_name='Range')),
                ('legal_pid', models.PositiveIntegerField(blank=True, null=True, verbose_name='PID')),
                ('well_location_description', models.CharField(blank=True, max_length=500, verbose_name='Well Location Description')),
                ('identification_plate_number', models.PositiveIntegerField(blank=True, null=True, unique=True)),
                ('well_tag_number', models.PositiveIntegerField(blank=True, null=True, unique=True)),
                ('diameter', models.CharField(blank=True, max_length=9)),
                ('total_depth_drilled', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('finished_well_depth', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('well_yield', models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True)),
            ],
            options={
                'db_table': 'gwells_well',
            },
        ),
        migrations.CreateModel(
            name='WellSubclass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=100)),
                ('is_hidden', models.BooleanField(default=False)),
                ('sort_order', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'gwells_well_subclass',
                'ordering': ['sort_order', 'description'],
            },
        ),
        migrations.RenameModel(
            old_name='WellUse',
            new_name='IntendedWaterUse',
        ),
        migrations.RenameModel(
            old_name='ClassOfWell',
            new_name='WellClass',
        ),
        migrations.RemoveField(
            model_name='subclassofwell',
            name='class_of_well',
        ),
        migrations.RemoveField(
            model_name='wellactivity',
            name='class_of_well',
        ),
        migrations.RemoveField(
            model_name='wellactivity',
            name='driller_responsible',
        ),
        migrations.RemoveField(
            model_name='wellactivity',
            name='legal_land_district',
        ),
        migrations.RemoveField(
            model_name='wellactivity',
            name='subclass_of_well',
        ),
        migrations.RemoveField(
            model_name='wellactivity',
            name='well_activity_type',
        ),
        migrations.RemoveField(
            model_name='wellactivity',
            name='well_use',
        ),
        migrations.RemoveField(
            model_name='wellactivity',
            name='well_yield_unit',
        ),
        migrations.RemoveField(
            model_name='wellowner',
            name='province_state',
        ),
        migrations.RemoveField(
            model_name='wellowner',
            name='well_activity',
        ),
        migrations.AlterModelTable(
            name='intendedwateruse',
            table='gwells_intended_water_use',
        ),
        migrations.AlterModelTable(
            name='wellclass',
            table='gwells_well_class',
        ),
        migrations.DeleteModel(
            name='SubclassOfWell',
        ),
        migrations.DeleteModel(
            name='WellActivity',
        ),
        migrations.DeleteModel(
            name='WellOwner',
        ),
        migrations.AddField(
            model_name='wellsubclass',
            name='well_class',
            field=models.ForeignKey(blank=True, db_column='gwells_well_class_id', on_delete=django.db.models.deletion.CASCADE, to='gwells.WellClass'),
        ),
        migrations.AddField(
            model_name='well',
            name='intended_water_use',
            field=models.ForeignKey(blank=True, db_column='gwells_intended_water_use_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.IntendedWaterUse', verbose_name='Water Supply Well Intended Water Use'),
        ),
        migrations.AddField(
            model_name='well',
            name='legal_land_district',
            field=models.ForeignKey(blank=True, db_column='gwells_legal_land_district_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.LandDistrict', verbose_name='Land District'),
        ),
        migrations.AddField(
            model_name='well',
            name='owner_province_state',
            field=models.ForeignKey(blank=True, db_column='gwells_province_state_id', on_delete=django.db.models.deletion.CASCADE, to='gwells.ProvinceState', verbose_name='Province'),
        ),
        migrations.AddField(
            model_name='well',
            name='well_class',
            field=models.ForeignKey(db_column='gwells_well_class_id', on_delete=django.db.models.deletion.CASCADE, to='gwells.WellClass', verbose_name='Well Class'),
        ),
        migrations.AddField(
            model_name='well',
            name='well_subclass',
            field=models.ForeignKey(blank=True, db_column='gwells_well_subclass_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.WellSubclass', verbose_name='Well Subclass'),
        ),
        migrations.AddField(
            model_name='well',
            name='well_yield_unit',
            field=models.ForeignKey(blank=True, db_column='gwells_well_yield_unit_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.WellYieldUnit'),
        ),
        migrations.AddField(
            model_name='ltsaowner',
            name='well',
            field=models.ForeignKey(blank=True, db_column='gwells_well_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.Well'),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='intended_water_use',
            field=models.ForeignKey(blank=True, db_column='gwells_intended_water_use_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.IntendedWaterUse', verbose_name='Water Supply Well Intended Water Use'),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='legal_land_district',
            field=models.ForeignKey(blank=True, db_column='gwells_legal_land_district_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.LandDistrict', verbose_name='Land District'),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='owner_province_state',
            field=models.ForeignKey(blank=True, db_column='gwells_province_state_id', on_delete=django.db.models.deletion.CASCADE, to='gwells.ProvinceState', verbose_name='Province'),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='well',
            field=models.ForeignKey(db_column='gwells_well_id', on_delete=django.db.models.deletion.CASCADE, to='gwells.Well'),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='well_activity_type',
            field=models.ForeignKey(db_column='gwells_well_activity_type_id', on_delete=django.db.models.deletion.CASCADE, to='gwells.WellActivityType', verbose_name='Type of Work'),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='well_class',
            field=models.ForeignKey(db_column='gwells_well_class_id', on_delete=django.db.models.deletion.CASCADE, to='gwells.WellClass', verbose_name='Well Class'),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='well_subclass',
            field=models.ForeignKey(blank=True, db_column='gwells_well_subclass_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.WellSubclass', verbose_name='Well Subclass'),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='well_yield_unit',
            field=models.ForeignKey(blank=True, db_column='gwells_well_yield_unit_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.WellYieldUnit'),
        ),
    ]