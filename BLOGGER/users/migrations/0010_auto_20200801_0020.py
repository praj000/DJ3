# Generated by Django 3.0.7 on 2020-07-31 18:50

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0009_auto_20200731_2331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='Fname',
        ),
        migrations.RemoveField(
            model_name='person',
            name='Lname',
        ),
        migrations.AddField(
            model_name='person',
            name='Name',
            field=models.OneToOneField(default='None', on_delete=django.db.models.deletion.CASCADE, related_name='name', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='person',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 8, 1, 0, 20, 21, 895160)),
        ),
    ]
