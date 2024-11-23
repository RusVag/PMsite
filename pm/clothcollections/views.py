from django.shortcuts import redirect, render
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from .models import *
# from .forms import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
# Create your views here.

def index(request):
    collection = Collection.objects.all()

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    print(request.session.session_key)

    return render(request, 'colls/collections.html', locals())



def CollInfo(request, slug):
    coll = Collection.objects.get(slug=slug)
    itemincoll = ItemInCollections.objects.filter(collection__id=coll.id)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print('SESSION KEY: ', request.session.session_key)
    return render(request, 'colls/details_coll.html', locals())