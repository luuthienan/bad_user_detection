# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 13:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sendo', '0003_salesorderdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipment_date', models.DateTimeField(null=True)),
                ('delivery_status', models.CharField(default='', max_length=256)),
                ('delivery_status_date', models.DateTimeField(null=True)),
                ('created_date', models.DateTimeField(null=True)),
                ('sales_order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sendo.SalesOrder')),
            ],
        ),
    ]
