# Generated by Django 2.2 on 2020-10-10 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0007_auto_20200905_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]