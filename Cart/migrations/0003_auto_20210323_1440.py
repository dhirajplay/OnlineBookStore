# Generated by Django 3.1.2 on 2021-03-23 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0002_deal_order_productinorder'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='order',
            table='Order',
        ),
    ]