# Generated by Django 2.1.2 on 2019-02-23 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tom_targets', '0006_merge_20190223_0219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='targetextra',
            name='bool_value',
        ),
        migrations.RemoveField(
            model_name='targetextra',
            name='float_value',
        ),
        migrations.RemoveField(
            model_name='targetextra',
            name='time_value',
        ),
    ]
