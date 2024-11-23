from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class User(AbstractUser, models.Model):
    first_name = models.CharField('Имя', null=True, max_length=30)
    last_name = models.CharField('Фамилия', null=True, max_length=30)
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True, null=True, verbose_name='Фото профиля',)
