from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from apitest.models import Apitest,Apistep


# Create your views here.

def test(request):
    return HttpResponse('hello test')


def login(request):
    if request.POST:
        # 获取用户名密码
        username = password = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        # auth进行用户信息认证
        user = auth.authenticate(username=username, password=password)
        # 校验用户名和密码的真实性
        if user is not None and user.is_active:
            # 登录
            auth.login(request, user)
            # session中的用户
            request.session['user'] = username
            response = HttpResponseRedirect('/home/')
            return response
        else:
            return render(request, 'login.html', {'error': 'username or password is error'})

    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')


def logout(request):
    auth.logout(request)
    return render(request, 'login.html')

# 接口管理
@login_required
def apitest_manage(request):
    # 读取所有流程接口数据
    apitest_list = Apitest.objects.all()
    # 读取浏览器登录Session,获取用户名
    username = request.session.get('user','')
    # 定义流程接口数据的变量并返回到前端
    return render(request,'apitest_manage.html',{"user":username,"apitests":apitest_list})

# 接口步骤用例管理
@login_required
def apistep_manage(request):
    username = request.session.get('user','')
    apistep_list = Apistep.objects.all()
    return render(request,'apistep_manage.html',{"user":username,"apisteps":apistep_list})


