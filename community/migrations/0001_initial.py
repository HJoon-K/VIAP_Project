# Generated by Django 4.0.5 on 2022-07-07 17:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('join', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rboard',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('workjum', models.IntegerField(default=0)),
                ('supjum', models.IntegerField(default=0)),
                ('regdate', models.DateTimeField(default=datetime.datetime.now)),
                ('contents', models.TextField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='join.member')),
            ],
            options={
                'db_table': 'rboard',
            },
        ),
    ]