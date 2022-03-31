from django.shortcuts import render
from . import models, forms

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

@login_required
def other(request):
    return render(request, 'basic_app/other.html')

def reg_form(request):
    form1 = forms.UserForm()
    form2 = forms.UserProfileInfoForm()
    registered = False
    if request.method == 'POST':
        form1 = forms.UserForm(request.POST)
        form2 = forms.UserProfileInfoForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            user.set_password(user.password)
            user.save()

            profile = form2.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(form1.errors,form2.errors)


    dict ={'form1':form1,'form2':form2, 'registered':registered}

    return render(request, 'basic_app/register.html',context=dict)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('ACCTOUNT NOT ACTIVE')
        else:
            print("Username: {} and password: {} failed login attempt".format(username,password))
    return render(request, 'basic_app/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
