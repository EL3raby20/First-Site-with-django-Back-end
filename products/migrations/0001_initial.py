# Generated by Django 3.2 on 2022-09-20 04:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('img', models.ImageField(upload_to='Brands/', verbose_name='Image')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('img', models.ImageField(upload_to='Brands/', verbose_name='Image')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('sku', models.IntegerField(verbose_name='sku')),
                ('subtitle', models.CharField(max_length=500, verbose_name='SubTitle')),
                ('descriptin', models.TextField(max_length=5000, verbose_name='Descriptin')),
                ('flag', models.CharField(choices=[('new', 'new'), ('sale', 'sale')], max_length=20, verbose_name='Flag')),
                ('price', models.FloatField(verbose_name='Price')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Products_brand', to='products.brand')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Products_Category', to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='Reviwes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(max_length=500, verbose_name='Review')),
                ('rate', models.IntegerField(verbose_name='Rate')),
                ('Create_at', models.TimeField(default=django.utils.timezone.now, verbose_name='Create_at')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_review', to='products.products', verbose_name='product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_review', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='ProductsImges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='productimg/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Products_image', to='products.products')),
            ],
        ),
    ]
