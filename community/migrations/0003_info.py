# Generated by Django 3.2.13 on 2022-07-14 12:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_alter_rboard_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('member', models.TextField()),
                ('e_add', models.TextField()),
                ('regdate', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'Info',
                'ordering': ['-id'],
            },
        ),
    ]
