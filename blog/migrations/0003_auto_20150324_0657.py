# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_campanhas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campanhas',
            old_name='emai',
            new_name='email',
        ),
    ]
