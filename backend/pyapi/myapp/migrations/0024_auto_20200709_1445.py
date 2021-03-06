# Generated by Django 3.0.8 on 2020-07-09 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_auto_20200708_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='edited',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='edited',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=250),
        ),
    ]
