# Generated by Django 3.0.8 on 2020-07-08 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_comment_parent_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='parent_id',
            field=models.CharField(max_length=50),
        ),
    ]
