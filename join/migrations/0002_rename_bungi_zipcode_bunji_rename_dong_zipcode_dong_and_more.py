# Generated by Django 4.0.5 on 2022-07-11 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='zipcode',
            old_name='BUNGI',
            new_name='bunji',
        ),
        migrations.RenameField(
            model_name='zipcode',
            old_name='DONG',
            new_name='dong',
        ),
        migrations.RenameField(
            model_name='zipcode',
            old_name='GUGUN',
            new_name='gugun',
        ),
        migrations.RenameField(
            model_name='zipcode',
            old_name='RI',
            new_name='ri',
        ),
        migrations.RenameField(
            model_name='zipcode',
            old_name='SIDO',
            new_name='sido',
        ),
        migrations.RenameField(
            model_name='zipcode',
            old_name='ZIPCODE',
            new_name='zipcode',
        ),
    ]