# Generated by Django 2.2 on 2020-08-30 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker_profile', '0022_auto_20200830_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workerprofile',
            name='social_networks',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='type'),
        ),
    ]
