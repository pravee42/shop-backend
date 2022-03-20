# Generated by Django 4.0.3 on 2022-03-14 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_email', models.CharField(max_length=200)),
                ('bill_number', models.IntegerField()),
                ('date', models.CharField(max_length=200)),
                ('product_name', models.CharField(max_length=200)),
                ('product_price', models.IntegerField()),
                ('product_qty', models.IntegerField()),
                ('product_gst', models.FloatField()),
                ('total_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CashInHand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_email', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('ammount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_email', models.CharField(max_length=200)),
                ('product_name', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('product_price', models.IntegerField()),
                ('product_qty', models.IntegerField()),
                ('product_gst', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_email', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('service_number', models.IntegerField()),
                ('service_name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('product_gst', models.FloatField()),
                ('total_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ServiceTotal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_email', models.CharField(max_length=200)),
                ('service_number', models.IntegerField()),
                ('date', models.CharField(max_length=200)),
                ('total_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TotalBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_email', models.CharField(max_length=200)),
                ('bill_number', models.IntegerField()),
                ('date', models.CharField(max_length=200)),
                ('total_ammount', models.IntegerField()),
            ],
        ),
    ]