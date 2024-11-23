from django.shortcuts import redirect, render
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

# Create your views here.
@csrf_protect
def index(request, cat_slug=None):
    context = {
        'item': ClothItem.objects.all(),
        'categories' : KindOfClothing.objects.all(),
    }
    if cat_slug:
        context.update({'item':ClothItem.objects.filter(typeName__kind__slug=cat_slug)})
    else:
        context.update({'item':ClothItem.objects.all()})

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    print(request.session.session_key)

    return render(request, 'catalog/catalog.html', context)



@csrf_protect
@login_required
def addItem(request):
    if request.user.is_superuser:
        if request.method=='POST':
            form = AddItemForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('catalog:index')
        form = AddItemForm()
        data = {
            'form':form,
        }
        return render(request, 'catalog/add_item.html', data)
    else:
        return redirect('catalog:index')



def ItemInfo(request, slug):
    item = ClothItem.objects.get(slug=slug)
        
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print('SESSION KEY: ', request.session.session_key)
    return render(request, 'catalog/details_item.html', locals())



