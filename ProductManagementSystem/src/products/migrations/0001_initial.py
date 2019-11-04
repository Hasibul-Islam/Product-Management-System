# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-16 09:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_name', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=200)),
                ('company_address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('wighth', models.DecimalField(decimal_places=2, max_digits=5)),
                ('style', models.CharField(blank=True, max_length=100, null=True)),
                ('color', models.CharField(max_length=100)),
                ('amount', models.PositiveIntegerField()),
                ('cotton', models.PositiveIntegerField(blank=True, null=True)),
                ('asking_price', models.PositiveIntegerField()),
                ('order_date', models.DateField()),
                ('delivery_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(max_length=100)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.ProductType'),
        ),
    ]
