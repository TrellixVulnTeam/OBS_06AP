# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-24 13:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('obs_semester', '__first__'),
        ('obs_department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accept_date', models.CharField(max_length=15)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obs_department.Department')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obs_semester.Semester')),
            ],
            options={
                'verbose_name': 'E\u011fitim Plan\u0131',
                'verbose_name_plural': 'E\u011fitim Planlar\u0131',
            },
        ),
    ]
