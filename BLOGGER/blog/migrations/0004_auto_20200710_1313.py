# Generated by Django 3.0.7 on 2020-07-10 07:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_posts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='auth',
            new_name='author',
        ),
        migrations.AlterField(
            model_name='posts',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 10, 7, 42, 58, 244572, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(max_length=400),
        ),
    ]
