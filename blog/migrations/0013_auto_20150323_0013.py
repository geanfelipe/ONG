# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_page_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='autor',
            field=models.ForeignKey(to='blog.Autores'),
            preserve_default=True,
        ),
    ]
