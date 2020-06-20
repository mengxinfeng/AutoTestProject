from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth


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
