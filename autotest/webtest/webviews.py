from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from webtest.models import Webcase, Webcasestep


# Create your views here.

@login_required
def webcase_manage(request):
    webcasse_list = Webcase.objects.all()
    username = request.session.get('user', '')
    return render(request, 'webcase_manage.html', {"user": username, "webcases": webcasse_list})


@login_required
def webcasestep_manage(request):
    webcasestep_list = Webcasestep.objects.all()
    username = request.session.get('user', '')
    return render(request, 'webcasestep_manage.html', {"user": username, "webcasesteps": webcasestep_list})
