# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150212_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='url',
            field=models.SlugField(unique=True, max_length=100),
            preserve_default=True,
        ),
    ]
