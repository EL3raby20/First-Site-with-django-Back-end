# Generated by Django 4.1.1 on 2022-09-28 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='code',
            field=models.CharField(default='75520300', max_length=9),
        ),
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='31114814', max_length=9),
        ),
    ]