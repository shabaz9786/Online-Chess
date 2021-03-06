# Generated by Django 3.0.8 on 2020-07-09 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0031_rate_comment_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate',
            name='id',
        ),
        migrations.AlterField(
            model_name='rate',
            name='comment_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Comment'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='username',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]
