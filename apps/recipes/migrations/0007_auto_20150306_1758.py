# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_auto_20150306_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='monsters',
            field=models.ManyToManyField(to='recipes.Monster', null=True),
            preserve_default=True,
        ),
    ]
