# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campanhas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=128)),
                ('emai', models.EmailField(max_length=75)),
                ('mensagem', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
