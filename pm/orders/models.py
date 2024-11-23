from django.db import models
from catalog.models import ClothItem
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField
User = get_user_model()

# Create your models here.


class Status(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True, default=None, verbose_name='Статус')
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы заказа'

class Order(models.Model):
    phone = PhoneNumberField('Номер телефона', max_length=12)
    customer = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Покупатель')
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name='Статус заказа')
    created = models.DateTimeField('Дата покупки', auto_now_add=True, auto_now=False)
    updated = models.DateTimeField('Дата изменения', auto_now_add=False, auto_now=True)
    address = models.TextField('Адрес доставки', blank=False, null=False, max_length=200)
    total_price = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    # def total_price(self):
    #     return sum([
    #         order_item.total()
    #         for order_item in ProductInOrder.objects.filter(order=self)
    #     ])
        
    def __str__(self):
        return f"{self.customer.username}, {self.customer.first_name} {self.customer.last_name}, {self.total_price}₽, {self.status}, {self.created}"
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def save(self, *args, **kwargs):

        super(Order, self).save(*args, **kwargs)


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)   
    item = models.ForeignKey(ClothItem, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name='Товар')
    count = models.IntegerField('Количество', blank=False, null=False, default=1)
    size = models.CharField('Размер', blank=True, null=True, max_length=20)
    is_active = models.BooleanField(default=True)

    price_per_item = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=0, default=0)#price*nmb

    def __str__(self):
        return f"{self.order.id}, {self.item.name} {self.count}, {self.price_per_item}, {self.total_price}₽"
    

    # def total(self):
    #     return self.count * self.item.price
    

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def save(self, *args, **kwargs):
        price_per_item = self.item.price
        self.price_per_item = price_per_item
        print (self.count)

        self.total_price = int(self.count) * price_per_item

        super(ProductInOrder, self).save(*args, **kwargs)





def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)

    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


post_save.connect(product_in_order_post_save, sender=ProductInOrder)


class ProductInBasket(models.Model):
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name='Заказ')   
    item = models.ForeignKey(ClothItem, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name='Товар')
    count = models.IntegerField('Количество', default=1, blank=False, null=False)
    size = models.CharField('Размер', blank=True, null=True, max_length=20)
    is_active = models.BooleanField(default=True)

    price_per_item = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=0, default=0)#price*nmb

    # def total(self):
    #     return self.count * self.item.price
    

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    def save(self, *args, **kwargs):
        price_per_item = self.item.price
        self.price_per_item = price_per_item

        self.total_price = int(self.count) * price_per_item

        super(ProductInBasket, self).save(*args, **kwargs)