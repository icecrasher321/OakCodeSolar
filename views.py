
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import *
from .models import *

def register(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserInfoForm()

    return render(request, 'registration/register.html', {'form': form})

def Dashboard(request):

    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        HttpResponse("Please Log In")
        return redirect('login')

def site_view(request):
    if request.method == 'POST':
        form = SiteForm(request.POST, instance = request.user)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.User = request.user
            stock.save()
            return redirect('/dashboard')

    else:
        form = SiteForm(instance = request.user)
    args = {'form': form}
    return render(request, 'site.html', args)

