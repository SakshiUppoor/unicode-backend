# Generated by Django 2.2.4 on 2019-08-16 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('launches', '0002_auto_20190816_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='launches',
            name='article_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='launches',
            name='details',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='launches',
            name='launch_success',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='launches',
            name='mission_patch_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='launches',
            name='reddit_launch',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='launches',
            name='rocket_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='launches',
            name='video_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='launches',
            name='wikipedia',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
