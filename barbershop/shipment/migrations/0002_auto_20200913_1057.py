# Generated by Django 2.2.14 on 2020-09-13 07:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shipment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shipment',
            old_name='user_address',
            new_name='buyer_address',
        ),
        migrations.RenameField(
            model_name='shipment',
            old_name='user_email',
            new_name='buyer_email',
        ),
        migrations.RenameField(
            model_name='shipment',
            old_name='user_name',
            new_name='buyer_name',
        ),
        migrations.RenameField(
            model_name='shipment',
            old_name='user_phone',
            new_name='buyer_phone',
        ),
        migrations.RenameField(
            model_name='shipment',
            old_name='user_surname',
            new_name='buyer_surname',
        ),
        migrations.RemoveField(
            model_name='shipment',
            name='user_comment',
        ),
        migrations.AddField(
            model_name='shipment',
            name='buyer_comment',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AddField(
            model_name='shipment',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipment_shipment_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Ким створено'),
        ),
        migrations.AddField(
            model_name='shipment',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 9, 13, 7, 57, 47, 857856, tzinfo=utc), verbose_name='Коли створено'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shipment',
            name='updated_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipment_shipment_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Ким змінено'),
        ),
        migrations.AddField(
            model_name='shipment',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, verbose_name='Коли змінено'),
        ),
    ]