# Generated by Django 2.1 on 2018-08-03 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_auto_20180803_2034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='time',
            new_name='registered_time',
        ),
    ]
