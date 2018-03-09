# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-09 10:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('app_code', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='\u552f\u4e00\u7f16\u7801')),
                ('app_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='\u5e94\u7528\u7cfb\u7edf\u540d\u79f0')),
                ('app_ip', models.CharField(blank=True, max_length=50, null=True, verbose_name='ip\u5730\u5740')),
                ('app_port', models.CharField(blank=True, max_length=50, null=True, verbose_name='\u7aef\u53e3')),
                ('city_code', models.CharField(blank=True, max_length=256, null=True, verbose_name='\u6240\u5c5e\u5730\u5e02')),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6dfb\u52a0\u65e5\u671f')),
            ],
            options={
                'db_table': 't_app',
            },
        ),
        migrations.CreateModel(
            name='AppList',
            fields=[
                ('app_code', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='\u552f\u4e00\u7f16\u7801')),
                ('app_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='\u5e94\u7528\u7cfb\u7edf\u540d\u79f0')),
                ('app_ip', models.CharField(blank=True, max_length=50, null=True, verbose_name='ip\u5730\u5740')),
                ('app_port', models.CharField(blank=True, max_length=50, null=True, verbose_name='\u7aef\u53e3')),
                ('city_code', models.CharField(blank=True, max_length=256, null=True, verbose_name='\u6240\u5c5e\u5730\u5e02')),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6dfb\u52a0\u65e5\u671f')),
            ],
            options={
                'db_table': 't_app_list',
            },
        ),
    ]
