# Generated by Django 4.1.7 on 2023-02-22 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goobusinessesapp', '0015_internalvisit'),
    ]

    operations = [
        migrations.AddField(
            model_name='clickhistry',
            name='timee',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='clickhistry',
            name='userAuthDt',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]