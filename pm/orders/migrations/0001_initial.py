# Generated by Django 5.1 on 2024-10-16 02:15

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=12, region=None, verbose_name='Номер телефона')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата покупки')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('address', models.TextField(max_length=200, verbose_name='Адрес доставки')),
                ('total_price', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='ProductInBasket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(blank=True, default=None, max_length=128, null=True)),
                ('count', models.IntegerField(default=1, verbose_name='Количество')),
                ('size', models.CharField(blank=True, max_length=20, null=True, verbose_name='Размер')),
                ('is_active', models.BooleanField(default=True)),
                ('price_per_item', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('total_price', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
            ],
            options={
                'verbose_name': 'Товар в корзине',
                'verbose_name_plural': 'Товары в корзине',
            },
        ),
        migrations.CreateModel(
            name='ProductInOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1, verbose_name='Количество')),
                ('size', models.CharField(blank=True, max_length=20, null=True, verbose_name='Размер')),
                ('is_active', models.BooleanField(default=True)),
                ('price_per_item', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('total_price', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
            ],
            options={
                'verbose_name': 'Товар в заказе',
                'verbose_name_plural': 'Товары в заказе',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=30, null=True, verbose_name='Статус')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы заказа',
            },
        ),
    ]
