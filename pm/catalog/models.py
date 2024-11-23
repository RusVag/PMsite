from django.db import models
from django.urls import reverse
from pytils.translit import slugify
# Create your models here.

class KindOfClothing(models.Model):
    kindName = models.CharField('Тип одежды', max_length=50, null=False, unique=True, blank=False)
    slug = models.SlugField(max_length=100, unique=False, null=False, blank=False, db_index=True)
    is_active = models.BooleanField(default=True)


    def __str__(self) -> str:
        return f'{self.kindName}'
    
    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"     

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug':self.kindName})
        
    def save(self, *args, **kwargs):
       self.slug = slugify(self.kindName)
       super(KindOfClothing, self).save(*args, **kwargs)

class TypeOfClothing(models.Model):
    typeName = models.CharField('Вид одежды', max_length=50, null=False, unique=True, blank=False)
    kind = models.ForeignKey(KindOfClothing, verbose_name='Тип одежды', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.kind}, {self.typeName}'
    
    class Meta:
        verbose_name = "Вид"
        verbose_name_plural = "Виды"    
    



class ClothItem(models.Model):
    NOSIZE = None
    TOP = 'top'
    BOTTOM = 'bottom'
    SIZE_CHOICE = [
        (NOSIZE, 'Без размера'),
        (TOP, 'Размеры для верха'),
        (BOTTOM, 'Размеры для низа'),
    ]

    name = models.CharField('Название', max_length=50, null=False)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=0, null=False, unique=False)
    # kindName = models.ForeignKey(KindOfClothing, verbose_name='Тип', null=False, on_delete=models.CASCADE)
    typeName = models.ForeignKey(TypeOfClothing, verbose_name='Вид', null=False, on_delete=models.CASCADE)
    description = models.TextField('Описание', max_length=1000, null=True, unique=False)
    frontpic = models.ImageField('Фото спереди', upload_to='items/%Y/%m/', blank=True, null=True)
    backpic = models.ImageField('Фото сзади', upload_to='items/%Y/%m/', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Дата добавления', auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True, null=False, blank=False, db_index=True)
    size_choice = models.CharField('Выбор размера', max_length=30, choices=SIZE_CHOICE, default='NOSIZE', blank=True, null=True)
    is_active = models.BooleanField(default=True)


    def __str__(self) -> str:
        return f'{self.typeName} - "{self.name}" - {self.price}₽'
    
    def get_absolute_url(self):
        return reverse('details', kwargs={'slug':self.name})
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        
    def save(self, *args, **kwargs):
       self.slug = slugify(self.name)
       super(ClothItem, self).save(*args, **kwargs)


    