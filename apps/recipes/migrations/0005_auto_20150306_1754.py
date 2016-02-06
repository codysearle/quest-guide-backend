# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_quest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='quest',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='quest',
            name='monsters',
            field=models.ManyToManyField(to='recipes.Monster', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='quest',
            name='objective',
            field=models.CharField(help_text=b'Main Quest Objective', max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='quest',
            name='subquest',
            field=models.CharField(help_text=b'Subquest Requirements', max_length=100),
            preserve_default=True,
        ),
    ]
