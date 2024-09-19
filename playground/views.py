from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#req->res request handler


def say_hello(req):
    return render(req, 'hello.html')