# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-06 13:02
from __future__ import unicode_literals

from django.db import migrations


def convert_lines_data(apps, schema_editor):
    CartLine = apps.get_model('checkout', 'CartLine')
    # Iterate over all cart lines, due to wrong JSONField None handling
    for line in CartLine.objects.all():
        if line.data is None:
            line.data = {}
            line.save(update_fields=['data'])


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20161014_1221'),
    ]

    replaces = [
        ('cart', 'fix_empty_data_in_lines'),
    ]

    operations = [
        migrations.RunPython(convert_lines_data, migrations.RunPython.noop)
    ]
