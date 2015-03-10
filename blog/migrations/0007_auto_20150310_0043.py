# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150223_2328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='body',
        ),
        migrations.AddField(
            model_name='page',
            name='description',
            field=models.TextField(default=datetime.datetime(2015, 3, 10, 3, 43, 4, 535286, tzinfo=utc), max_length=240),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='page',
            name='when',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'data de cria\xc3\xa7\xc3\xa3o', db_index=True),
            preserve_default=True,
        ),
    ]
