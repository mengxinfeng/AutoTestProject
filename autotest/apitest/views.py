from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def test(request):
    return HttpResponse('hello test')


def login(request):
    return render(request, 'login.html')
