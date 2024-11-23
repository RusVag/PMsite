# Generated by Django 5.1 on 2024-10-16 02:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KindOfClothing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kindName', models.CharField(max_length=50, unique=True, verbose_name='Тип одежды')),
                ('slug', models.SlugField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Типы',
            },
        ),
        migrations.CreateModel(
            name='TypeOfClothing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeName', models.CharField(max_length=50, unique=True, verbose_name='Вид одежды')),
                ('is_active', models.BooleanField(default=True)),
                ('kind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.kindofclothing', verbose_name='Тип одежды')),
            ],
            options={
                'verbose_name': 'Вид',
                'verbose_name_plural': 'Виды',
            },
        ),
        migrations.CreateModel(
            name='ClothItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Цена')),
                ('description', models.TextField(max_length=800, null=True, verbose_name='Описание')),
                ('frontpic', models.ImageField(blank=True, null=True, upload_to='items/%Y/%m/', verbose_name='Фото спереди')),
                ('backpic', models.ImageField(blank=True, null=True, upload_to='items/%Y/%m/', verbose_name='Фото сзади')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('size_choice', models.CharField(blank=True, choices=[(None, 'Без размера'), ('top', 'Размеры для верха'), ('bottom', 'Размеры для низа')], default='NOSIZE', max_length=30, null=True, verbose_name='Выбор размера')),
                ('is_active', models.BooleanField(default=True)),
                ('typeName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.typeofclothing', verbose_name='Вид')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
