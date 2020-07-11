from django.shortcuts import render
from apptest.models import Appcase,Appcasestep
from django.contrib.auth.decorators import login_required
# Create your views here.

# app用例管理
@login_required
def appcase_manage(request):
    username = request.session.get('user','')
    case_list = Appcase.objects.all()
    return render(request,'appcase_manage.html',{"user":username,"appcases":case_list})

# app测试用例步骤
@login_required
def appcasestep_manage(request):
    username = request.session.get('user', '')
    casestep_list = Appcasestep.objects.all()
    return render(request, 'appcasestep_manage.html', {"user": username, "appcasesteps": casestep_list})