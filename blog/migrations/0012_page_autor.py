# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_autores'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='autor',
            field=models.CharField(default=datetime.datetime(2015, 3, 23, 3, 12, 16, 24541, tzinfo=utc), max_length=128),
            preserve_default=False,
        ),
    ]
