# Generated by Django 3.0.7 on 2020-07-14 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='dec',
            field=models.CharField(default='ok', max_length=1221),
        ),
    ]
