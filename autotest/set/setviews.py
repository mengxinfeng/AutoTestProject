from django.contrib.auth.models import User
from django.shortcuts import render
from set.models import Set
# Create your views here.

# 系统设置
def set_manage(request):
    username = request.session.get('user','')
    set_list = Set.objects.all()
    return render(request,'set_manage.html',{"user":username,"sets":set_list})

# 用户管理
def user_manage(request):
    username = request.session.get('user','')
    user_list = User.objects.all()
    return render(request, 'user_manage.html', {"user": username, "users": user_list})