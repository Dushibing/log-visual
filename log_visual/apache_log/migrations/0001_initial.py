# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Access_Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('log_data', models.CharField(max_length=100)),
                ('access_ip', models.CharField(max_length=100)),
                ('access_url', models.CharField(max_length=150)),
                ('access_status', models.IntegerField()),
                ('blank_field1', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Error_Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('error_level', models.CharField(max_length=30)),
                ('error_ip', models.CharField(max_length=100)),
                ('error_content', models.TextField()),
                ('blank_error', models.CharField(max_length=30)),
            ],
        ),
    ]
