# Generated by Django 2.2 on 2020-08-16 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200816_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='type',
            field=models.CharField(choices=[('hair_cut', 'Hair Cut'), ('product', 'Product')], default='product', max_length=50),
        ),
    ]
