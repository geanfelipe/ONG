# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150212_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='denuncias',
            name='Category',
            field=models.CharField(default=django.utils.timezone.now, max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(unique=True, max_length=128, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(unique=True, max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='url',
            field=models.URLField(unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='when',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'date created', db_index=True),
            preserve_default=True,
        ),
    ]
