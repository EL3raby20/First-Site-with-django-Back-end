# Generated by Django 4.1.1 on 2022-09-29 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_cart_code_alter_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='code',
            field=models.CharField(default='83371271', max_length=9),
        ),
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='77224528', max_length=9),
        ),
    ]
