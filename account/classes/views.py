from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from datetime import datetime
from classes.models import *

def hello_world(request):
    return render(request, 'template_whoami.html', {'now': str(datetime.today()), })


def index(request):
    return render(request, 'index.html')

def get_signup(request):
    return render(request, 'signup.html')

def post_signup(request):
    uname = request.POST.get('uname')
    pw = request.POST.get('pw')
    rname = request.POST.get('rname')
    uemail = request.POST.get('uemail')
    user = Account.objects.create(username=uname, password=pw, realname=rname, useremail=uemail)
    if user:
        return redirect('/index', locals())
    else:
        return redirect('/signup', locals())
