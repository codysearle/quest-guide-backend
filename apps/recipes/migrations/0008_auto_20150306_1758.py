# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_auto_20150306_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='monsters',
            field=models.ManyToManyField(to='recipes.Monster'),
            preserve_default=True,
        ),
    ]