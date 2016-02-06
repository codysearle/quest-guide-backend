# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_quest_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingredients',
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Recipe',
        ),
        migrations.AddField(
            model_name='monster',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'photos', blank=True),
            preserve_default=True,
        ),
    ]
