# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='category',
            name='views',
        ),
        migrations.AddField(
            model_name='page',
            name='body',
            field=models.TextField(default=datetime.datetime(2015, 2, 12, 19, 51, 10, 791431, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='denuncias',
            name='text',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
