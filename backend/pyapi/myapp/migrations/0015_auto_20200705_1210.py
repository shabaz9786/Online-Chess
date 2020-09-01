# Generated by Django 3.0.8 on 2020-07-05 12:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20200705_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_id',
            field=models.CharField(blank=True, default='193887', max_length=50, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='posted_date',
            field=models.CharField(default=datetime.datetime(2020, 7, 5, 12, 10, 11, 706258), max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='last_posted_date',
            field=models.CharField(default=datetime.datetime(2020, 7, 5, 12, 10, 11, 705826), max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_id',
            field=models.CharField(blank=True, default='275C78', max_length=50, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='posted_date',
            field=models.CharField(default=datetime.datetime(2020, 7, 5, 12, 10, 11, 705788), max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(blank=True, default='A4BF04', max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]
