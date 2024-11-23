from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

# Create your views here.

@csrf_protect
def index(req):
    con = {
        'title': 'Post Mortem'
    }
    return render(req, 'home/home.html', con)