
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import *
from django.views.generic import TemplateView
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
        form = SiteForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.user = request.user
            post.save()
            return redirect('/dashboard')
        else:
            form = SiteForm()
    else:
        form = SiteForm()
    return render(request, 'site.html', {'form': form})


class site_view1(TemplateView):
    template_name = 'site.html'

    def get(self, request):
        form = SiteForm()
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = SiteForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            text = form.cleaned_data['user','site_name', 'city_name','ZIP_code', 'country_code','budget','area','power_req']
            form = SiteForm()
            return redirect('/dashboard')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)


def redir(request):
    return redirect('/dashboard')

def logout(request):
    auth_logout(request)
    return render(request, 'logged_out.html')

