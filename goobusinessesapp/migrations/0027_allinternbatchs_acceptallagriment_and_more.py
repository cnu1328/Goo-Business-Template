# Generated by Django 5.0 on 2024-02-14 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goobusinessesapp', '0026_transectionhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='allinternbatchs',
            name='AcceptAllAgriment',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='allinternbatchs',
            name='ResumePDF',
            field=models.FileField(blank=True, null=True, upload_to='Resumes'),
        ),
        migrations.AddField(
            model_name='allinternbatchs',
            name='lastUpdateTime',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='allinternbatchs',
            name='lastUpdatedate',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='allinternbatchs',
            name='otp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='allinternbatchs',
            name='otpStatus',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='registationformdb',
            name='AcceptAllAgriment',
            field=models.BooleanField(default=True),
        ),
    ]