# Generated by Django 4.1.1 on 2022-09-23 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20220922_0537'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='img',
            field=models.ImageField(default='', upload_to='Products/'),
            preserve_default=False,
        ),
    ]