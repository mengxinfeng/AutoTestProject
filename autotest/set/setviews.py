from django.shortcuts import render
from set.models import Set
# Create your views here.

def set_manage(request):
    username = request.session.get('user','')
    set_list = Set.objects.all()
    return render(request,'set_manage.html',{"user":username,"sets":set_list})