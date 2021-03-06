# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-08 03:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('image', models.ImageField(upload_to='banners/%Y/%m', verbose_name='图片')),
                ('url', models.CharField(blank=True, max_length=200, verbose_name='URL链接')),
                ('index', models.ImageField(default=100, upload_to='', verbose_name='顺序')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='上传时间')),
            ],
            options={
                'verbose_name': '轮播',
                'verbose_name_plural': '轮播',
            },
        ),
    ]
