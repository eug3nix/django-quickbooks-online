# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
try:
    from django_extensions.db.fields.encrypted import EncryptedCharField
except ImportError:
    from django_fields.fields import EncryptedCharField


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QuickbooksToken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('access_token', EncryptedCharField(max_length=255)),
                ('access_token_secret', EncryptedCharField(max_length=255)),
                ('realm_id', models.CharField(max_length=64)),
                ('data_source', models.CharField(max_length=10)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
