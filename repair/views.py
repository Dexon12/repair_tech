from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import *


def home_page_view(request):
    query = request.GET.get('query')
    if query:
        services = Services.objects.filter(title__icontains=query)
        return render(request, 'containers/home_page.html', {'services': services})
    else:
        services = Services.objects.all()
        return render(request, 'containers/home_page.html', {'services': services})


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken, choose another')
                return redirect('register_view')
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken, choose another')
                return redirect('register_view')
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.success(request, 'Account created successfully')
                return redirect('login_user')
        else:
            messages.error(request, 'Passwords do not match')
    else:
        return render(request, "registration/register.html")



def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home_view')
        else:
            messages.info(request, 'Invalid Username or password')
            return redirect(login_user)
    else:  
        return render(request, "registration/login.html")

def logout_user(request):
   auth.logout(request)
   return redirect('login_user')


def profile_view(request):
    return render(request, 'registration/user_profile.html')

def service_detail(request, service_slug):
    service = get_object_or_404(Services, slug=service_slug)

    return render(request, 'containers/service_detail.html', {'service': service})

def contacts_view(request):
    return render(request, 'containers/contacts.html')


def search_results(request):
    query = request.GET.get('q')
    if query:
        services = Services.objects.filter(title__icontains=query)
        if services:
            return redirect('home_view', query=query)
        else:
            messages.info(request, 'Ничего не найдено.')
    return redirect('home_view')


