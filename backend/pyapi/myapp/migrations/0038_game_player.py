# Generated by Django 3.0.8 on 2020-07-18 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0037_auto_20200718_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='player',
            field=models.CharField(default='', max_length=50),
        ),
    ]
