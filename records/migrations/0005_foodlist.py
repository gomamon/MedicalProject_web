# Generated by Django 2.1 on 2018-08-13 09:43

from django.db import migrations, models
import records.models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0004_auto_20180813_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to=records.models.custom_path)),
                ('foot_type', models.PositiveIntegerField(choices=[(1, '고체'), (2, '액체')])),
                ('amount', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]