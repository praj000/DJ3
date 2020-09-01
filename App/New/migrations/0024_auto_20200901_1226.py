# Generated by Django 3.0.7 on 2020-09-01 06:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('New', '0023_auto_20200901_1218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mobile',
            old_name='model_name',
            new_name='model',
        ),
        migrations.AlterField(
            model_name='car',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 1, 12, 26, 23, 973281), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='medical',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 1, 12, 26, 23, 975275), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 1, 12, 26, 23, 973281), verbose_name='Date'),
        ),
    ]
