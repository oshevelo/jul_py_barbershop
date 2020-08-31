# Generated by Django 2.2.14 on 2020-08-30 07:13

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0009_auto_20200828_0656'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products_product_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Ким створено'),
        ),
        migrations.AddField(
            model_name='product',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 8, 30, 7, 13, 31, 973024, tzinfo=utc), verbose_name='Коли створено'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='updated_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products_product_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Ким змінено'),
        ),
        migrations.AddField(
            model_name='product',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, verbose_name='Коли змінено'),
        ),
    ]
