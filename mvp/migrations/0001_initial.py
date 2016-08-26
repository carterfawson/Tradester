# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('taskid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=245)),
                ('phone', models.CharField(max_length=13)),
                ('zip', models.CharField(max_length=5)),
                ('task', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
