# Generated by Django 4.0.3 on 2022-03-17 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='product_id',
            field=models.IntegerField(default=0),
        ),
    ]