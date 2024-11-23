from django.db import models
from django.urls import reverse
from pytils.translit import slugify
from catalog.models import ClothItem

# Create your models here.
class Collection(models.Model):
    photo = models.ImageField('Фото коллекции', upload_to='collections/%Y/%m/', blank=True, null=True)
    name = models.CharField('Название', max_length=50, null=False, blank=False, unique=True, default=None)
    created = models.DateTimeField('Дата покупки', auto_now_add=True, auto_now=False)
    updated = models.DateTimeField('Дата изменения', auto_now_add=False, auto_now=True)

    slug = models.SlugField(max_length=100, unique=True, null=False, blank=False, db_index=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.id}, {self.name}, {self.created}, {self.updated}"

    def get_absolute_url(self):
        return reverse('index', kwargs={'slug':self.name})

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'


    def save(self, *args, **kwargs):
       self.slug = slugify(self.name)
       super(Collection, self).save(*args, **kwargs)


class ItemInCollections(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)   
    item = models.ForeignKey(ClothItem, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name='Товар')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.collection.id}, {self.collection.name} - {self.item.id}, {self.item.typeName.typeName}, {self.item.name}"
    
    
    def save(self, *args, **kwargs):

        super(ItemInCollections, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Товар в Коллекции'
        verbose_name_plural = 'Товары в Коллекции'
