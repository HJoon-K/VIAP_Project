# Generated by Django 4.0.5 on 2022-07-11 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0002_rename_bungi_zipcode_bunji_rename_dong_zipcode_dong_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='mailing',
        ),
    ]
