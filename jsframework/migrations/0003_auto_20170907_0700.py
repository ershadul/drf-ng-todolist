# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jsframework', '0002_remove_todo_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='session',
            field=models.CharField(db_index=True, max_length=32, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
