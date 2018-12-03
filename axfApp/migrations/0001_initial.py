# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-12-03 09:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryId', models.CharField(max_length=64)),
                ('categoryName', models.CharField(max_length=64)),
                ('sort', models.IntegerField()),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='ChildCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('childId', models.CharField(max_length=64)),
                ('childName', models.CharField(max_length=64)),
                ('sort', models.IntegerField()),
                ('isDelete', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='axfApp.Category')),
            ],
            options={
                'db_table': 'childcategories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('longName', models.CharField(max_length=128)),
                ('productId', models.CharField(max_length=64)),
                ('storeNums', models.IntegerField()),
                ('specifics', models.CharField(max_length=32)),
                ('sort', models.IntegerField()),
                ('marketPrice', models.FloatField()),
                ('price', models.FloatField()),
                ('categoryId', models.CharField(max_length=64)),
                ('childCid', models.CharField(max_length=64)),
                ('img', models.CharField(max_length=256)),
                ('keywords', models.CharField(max_length=256)),
                ('brandId', models.CharField(max_length=64)),
                ('brandName', models.CharField(max_length=64)),
                ('safeDay', models.CharField(max_length=64)),
                ('safeUnit', models.CharField(max_length=64)),
                ('safeUnitDesc', models.CharField(max_length=64)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]
