# Generated by Django 2.2 on 2020-10-10 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0008_auto_20201010_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
