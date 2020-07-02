from django.shortcuts import render

# Create your views here.

from product.models import Product

# 产品管理
def product_manage(request):
    username = request.session.get('user','')
    product_list = Product.objects.all()
    return render(request,"product_manage.html",{"user":username,"products":product_list})

