# Generated by Django 4.0.5 on 2022-07-11 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0003_remove_member_mailing'),
        ('question', '0004_alter_question_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='qname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='join.member'),
        ),
    ]