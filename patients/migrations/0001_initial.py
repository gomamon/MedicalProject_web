# Generated by Django 2.1 on 2018-08-03 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.PositiveIntegerField(unique=True)),
                ('name', models.CharField(max_length=10)),
                ('birth', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('liquid_amount', models.FloatField()),
                ('consume_amount', models.FloatField()),
                ('urine_amount', models.FloatField()),
                ('stool_count', models.PositiveIntegerField()),
            ],
        ),
    ]
