from .models import ProductInBasket
from django.views.decorators.csrf import csrf_protect


def getting_basket_info(request):
    session_key = request.session.session_key

    if not session_key:

        # request.session['session_key'] = 123
        
        request.session.cycle_key()

    products_in_basket =  ProductInBasket.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    products_amount =  products_in_basket.count()
    
    return locals()