# Generated by Django 4.1.1 on 2022-09-24 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_category_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]