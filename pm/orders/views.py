import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .forms import CheckoutContactForm
from django.contrib.auth import get_user_model
from users.forms import ProfileUserForm

# from orders.JsonImageEncoder import ImageFieldFileAwareJsonEncoder

@csrf_protect
def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print(request.POST)
    data = request.POST
    product_id = data.get('product_id')  # данные берутся из js/scripts.js
    product_count = data.get('nmb')
    is_delete = data.get('is_delete')
    size_select = data.get('size')

    if is_delete == 'true':
        ProductInBasket.objects.filter(id=product_id).update(is_active=False)
        # product = ProductInBasket.objects.get(id=product_id)
        # product.is_active=False
        # product.save(force_update=True)
    
    else:
        new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, item_id = product_id,
                                                                      is_active=True, order=None, defaults={'count': product_count, 'size':size_select})
        
        if not created: 
            print('not_created')
            new_product.count += int(product_count)
            new_product.save(force_update=True)

    # common code for 2 cases
    products_in_basket =  ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    products_amount =  products_in_basket.count()

    products_amount =  ProductInBasket.objects.filter(session_key=session_key, is_active=True).count()
    return_dict['products_amount'] = products_amount

    return_dict['products'] = list()

    for itemproduct in products_in_basket:
        imgfile = itemproduct.item.frontpic.url

        product_dict = dict()
        product_dict['item_img'] = imgfile

        product_dict['size'] = itemproduct.size
        product_dict['id'] = itemproduct.id
        product_dict['name'] = itemproduct.item.name
        product_dict['total_price'] = itemproduct.total_price
        product_dict['count'] = itemproduct.count
        return_dict['products'].append(product_dict)

    return JsonResponse(return_dict)

@login_required
def checkout(request):
    session_key = request.session.session_key
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True, order__isnull=True)

    
    form = CheckoutContactForm(request.POST or None)
    if request.POST:
        print(request.POST)
        if form.is_valid():
            print('yes')
            data = request.POST
            phone = data['phone']
            address = data['address']
            username = request.user.username #передает логин пользователя
            user = request.user

            order = Order.objects.create(customer=user, phone=phone, address=address, status_id=1)

            for name, value in data.items():
                if name.startswith('product_in_basket_'):
                    product_in_basket_id = name.split('product_in_basket_')[1]
                    product_in_basket = ProductInBasket.objects.get(id=product_in_basket_id)
                    product_in_basket.count = value
                    product_in_basket.order = order
                    product_in_basket.is_active = False

                    product_in_basket.save(force_update=True)

                    ProductInOrder.objects.create(item=product_in_basket.item, size=product_in_basket.size, count=product_in_basket.count, price_per_item=product_in_basket.price_per_item,
                                                  total_price=product_in_basket.total_price, order=order)
        else:
            print('no')


    return render(request, 'orders/checkout.html', locals())