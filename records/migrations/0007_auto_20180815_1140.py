# Generated by Django 2.1 on 2018-08-15 02:40

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0006_auto_20180813_1909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodlist',
            name='foot_type',
        ),
        migrations.AddField(
            model_name='record',
            name='data_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 15, 2, 40, 34, 306361, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='record',
            name='updated_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='io_type',
            field=models.PositiveIntegerField(choices=[(1, 'Input'), (2, 'Output')]),
        ),
        migrations.AlterField(
            model_name='record',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.Information'),
        ),
        migrations.AlterField(
            model_name='record',
            name='record_type',
            field=models.PositiveIntegerField(choices=[(1, '경구 (환자입력)'), (2, '경구 (간호사입력)'), (3, '경관 (간호사입력)'), (4, '정맥 주입 주사 1'), (5, '정맥 주입 주사 2'), (6, 'Self Voiding (환자입력)'), (7, 'Self Voiding (간호사입력)'), (8, 'Foley Catheter (환자입력)'), (9, 'Foley Catheter (간호사입력)'), (10, '대변 (환자입력)'), (11, '대변 (간호사입력)')]),
        ),
        migrations.AlterField(
            model_name='record',
            name='registered_time',
            field=models.DateTimeField(),
        ),
    ]
