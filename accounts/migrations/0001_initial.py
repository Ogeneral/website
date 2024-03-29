# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-01 06:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile_image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, null=True)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('email', models.CharField(default='', max_length=50, null=True)),
                ('phone', models.IntegerField(default=0, null=True)),
                ('Class', models.CharField(blank=True, max_length=50)),
                ('Class_teacher', models.CharField(blank=True, max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile_image')),
                ('School_fees_status', models.CharField(blank=True, max_length=58)),
                ('Admission_No', models.CharField(blank=True, max_length=50)),
                ('Number_of_time_present_and_absent_in_school', models.CharField(blank=True, max_length=50)),
                ('Total_number_in_class', models.CharField(blank=True, max_length=50)),
                ('Basic_Tech', models.CharField(blank=True, max_length=50, null=True)),
                ('Business_Studies', models.CharField(blank=True, max_length=50, null=True)),
                ('Home_Economics', models.CharField(blank=True, max_length=50, null=True)),
                ('Agric_Science', models.CharField(blank=True, max_length=50, null=True)),
                ('Physical_Education', models.CharField(blank=True, max_length=50, null=True)),
                ('Yoruba', models.CharField(blank=True, max_length=50, null=True)),
                ('French', models.CharField(blank=True, max_length=50, null=True)),
                ('Fine_Art', models.CharField(blank=True, max_length=50, null=True)),
                ('Basic_Science', models.CharField(blank=True, max_length=50, null=True)),
                ('Social_Studies', models.CharField(blank=True, max_length=50, null=True)),
                ('Senior_result', models.CharField(blank=True, max_length=50, null=True)),
                ('Mathematics', models.CharField(blank=True, max_length=50, null=True)),
                ('English_language', models.CharField(blank=True, max_length=50, null=True)),
                ('CRK', models.CharField(blank=True, max_length=50, null=True)),
                ('Physics_or_Office_practice', models.CharField(blank=True, max_length=50, null=True)),
                ('Chemistry_or_Insurance', models.CharField(blank=True, max_length=50, null=True)),
                ('Biology', models.CharField(blank=True, max_length=50, null=True)),
                ('Agriculture_Science', models.CharField(blank=True, max_length=50, null=True)),
                ('Commerce', models.CharField(blank=True, max_length=50, null=True)),
                ('Account', models.CharField(blank=True, max_length=50, null=True)),
                ('Government', models.CharField(blank=True, max_length=50, null=True)),
                ('Geography', models.CharField(blank=True, max_length=50, null=True)),
                ('Computer_Science', models.CharField(blank=True, max_length=50, null=True)),
                ('Literature_In_English', models.CharField(blank=True, max_length=50, null=True)),
                ('Further_Mathematics', models.CharField(blank=True, max_length=50, null=True)),
                ('Photography', models.CharField(blank=True, max_length=50, null=True)),
                ('Dyeing_and_Bleaching', models.CharField(blank=True, max_length=50, null=True)),
                ('Clothing_and_Textile', models.CharField(blank=True, max_length=50, null=True)),
                ('Food_and_Nutrition', models.CharField(blank=True, max_length=50, null=True)),
                ('Animal_Husbandry', models.CharField(blank=True, max_length=50, null=True)),
                ('Civic_Education', models.CharField(blank=True, max_length=50, null=True)),
                ('Student_Academic_Status25', models.CharField(blank=True, max_length=50, null=True)),
                ('Student_Academic_Status100', models.CharField(blank=True, max_length=50, null=True)),
                ('notifcations', models.CharField(blank=True, max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
