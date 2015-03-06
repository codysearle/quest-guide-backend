# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipe_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('objective', models.TextField(help_text=b'Main Quest Objective', null=True, blank=True)),
                ('subquest', models.TextField(help_text=b'Subquest Requirements')),
                ('photo', models.ImageField(null=True, upload_to=b'photos', blank=True)),
                ('ingredients', models.ManyToManyField(to='recipes.Ingredient')),
                ('tags', models.ManyToManyField(to='recipes.Tag')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
