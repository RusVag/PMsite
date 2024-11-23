$(document).ready(function () {
    var form = $('.form_buying_product');
    console.log(form);

    function basketUpdating(product_id, nmb, size, is_delete){
        var data = {};
        data.product_id = product_id;
        data.nmb = nmb;
        data.size = size;
        var csrf_token = $('.form_buying_product [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        if (is_delete){
            data['is_delete'] = true;
        }

        var url = form.attr('action');

        console.log(data);
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function(data) {
                if (data.products_amount || data.products_amount == 0){
                    $('#basket_products_amount').text('('+data.products_amount+')');
                    $('.basket-items ul').html('')

                    $.each(data.products, function(k, v){
                        $('.basket-items ul').append(
                            '<form method="post" class="form_buying_product" action="{% url "basket:basket_adding" %}">'+
                                '<li>'+
                                '<img src='+v.item_img+'>'+ v.name+' * '+v.count+'шт. = '+v.total_price+'₽'+
                                '<button type="submit" class="delete-item" data-product_id="'+v.id+'">'+
                                    '<svg width="20" height="20" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg">'+
                                        '<path fill-rule="evenodd" clip-rule="evenodd" d="M4.11 2.697L2.698 4.11 6.586 8l-3.89 3.89 1.415 1.413L8 9.414l3.89 3.89 1.413-1.415L9.414 8l3.89-3.89-1.415-1.413L8 6.586l-3.89-3.89z" fill="#000"></path>'+
                                    '</svg>'+
                                '</button>'+
                                '</li>'+
                            '</form>'
                        );
                    })

                }

            },
            error: function(){
                console.log('error')
            }
        });

    };


    form.on('submit', function (e) {
        e.preventDefault();

        var nmb = $('#countinput').val();
        var size = $('#size_select').val();
        
        var submit_btn = $('#submit_btn')
        var product_id = submit_btn.data('product_id'); // id продукта считываются с submit_btn
        var product_name = submit_btn.data('product_name'); //название продукта считываются с submit_btn
        var product_slug = submit_btn.data('product_slug'); //slug продукта считываются с submit_btn
        var product_price = submit_btn.data('product_price'); //цена продукта считываются с submit_btn
        var product_img = submit_btn.data('product_img'); //картинка продукта считываются с submit_btn(хз зачем, потом придумаю)

        basketUpdating(product_id, nmb, size, is_delete=false)
    });



    // CART SVG SHOW UP AND HIDE
    function showingBasket() {
        if ($('.basket-items').css('visibility') == 'visible') {
            $('.basket-items').css({ 'visibility': 'hidden' });
        } else {
            $('.basket-items').css({ 'visibility': 'visible' });
        };
    };
    
    $('.basket-button').click(function (e) {
        e.preventDefault();
        showingBasket();
    });


    // DELETING FROM BASKET/CART
    $(document).on('click', '.delete-item', function(e){
        // console.log('удаление из корзины');
        e.preventDefault();
        product_id = $(this).data('product_id')
        nmb = 0
        size = 'None'
        basketUpdating(product_id, nmb, size, is_delete=true)

        // console.log('удален из корзины');
    });


    // BASKET CHECKOUT
    function calcBasketAmount(){
        var total_order_amount = 0;
        $('.total_product_in_basket_amount').each(function(){
            total_order_amount = total_order_amount + parseFloat($(this).text());
            
        });
        
        $('#total_order_amount').text(total_order_amount);

    };

    $(document).on('change', '.product_in_basket_count', function(){    
        var current_count = $(this).val();

        var current_tr = $(this).closest('tr');
        var current_price = parseInt(current_tr.find('.product_price').text());

        var total_amount = parseInt(current_price*current_count);

        current_tr.find('.total_product_in_basket_amount').text(total_amount);



        calcBasketAmount();
    });

    calcBasketAmount();
});