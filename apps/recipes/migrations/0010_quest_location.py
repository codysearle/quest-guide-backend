# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_auto_20150309_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='location',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
    ]
