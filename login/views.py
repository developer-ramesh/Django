from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from .models import UserProfile, User
from django.contrib.auth.models import User

@csrf_protect
def register(request):
    log_message= None
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )

            log_message = 'success'
            context = {
        'log_message': log_message
    }
            return render(request,'registration/register.html',context)
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })

    return render_to_response(
    'registration/register.html',
    variables,
    )

@login_required
def profile(request):
         current_user = request.user
         if request.method == 'POST':
            current_user = request.user
            image = request.FILES['image']
            u = UserProfile(
            avatar = image,
            user_id=current_user.id,
            id=request.POST.get('id')
            )
            u.save()
            return render(request,'registration/profile_pic.html',{'msg':'Picture uploaded successfully'})
         else:
             user=UserProfile.objects.get(user_id=current_user.id)
             return render(request,'registration/profile_pic.html' , { 'user_profile': user , 'user':request.user, 'url':'profile' } )

def register_success(request):
    return render_to_response(
    'registration/success.html',
    )

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def menu(request):
    return render_to_response(
    'menu.html',
    { 'user': request.user , 'url':'menu'  }
    )


#def dologin(request):
#    log_message= None
#    if request.method == 'POST':
#        username = request.POST.get('username')
#        password = request.POST.get('password')
#        user = authenticate(username = username, password = password)
#        if user:
#            if user.is_active:
#                login(request, user)
#                return HttpResponseRedirect('/')
#            else:
#                log_message = 'Blocked by admin'
#        else:
#            log_message = 'Wrong username and password'
#   context = {
#        'log_message': log_message
#    }
#   return render(request,'registration/dologin.html',context)


def index(request):
    return render_to_response(
    'index.html',{ 'user': request.user , 'url':'home' }
    )

def about(request):
    return render_to_response(
    'cms/about.html',{ 'user': request.user,'url':'about' }
    )
