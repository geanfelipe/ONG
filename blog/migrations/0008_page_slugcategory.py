# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20150310_0043'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slugCategory',
            field=models.SlugField(default=datetime.datetime(2015, 3, 10, 5, 52, 2, 867252, tzinfo=utc), unique=True),
            preserve_default=False,
        ),
    ]
