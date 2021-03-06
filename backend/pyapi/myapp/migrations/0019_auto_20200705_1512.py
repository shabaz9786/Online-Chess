# Generated by Django 3.0.8 on 2020-07-05 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_auto_20200705_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='posted_date',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='last_posted_date',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='posted_date',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]
