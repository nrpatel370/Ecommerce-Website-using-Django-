from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from store.models import Product
from store.models import Customer

# Create your views here.
#req->res request handler


def say_hello(req):

    queryset = Product.objects.filter(Q(inventory__lt = 10) & Q(unit_price__lt = 20))
    
    
    return render(req, 'hello.html', {'products': list(queryset)})