from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *



class UserInfoForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('company_name', 'username', )

class SiteForm(forms.ModelForm):

    class Meta:
        model = Site
        fields = ('site_name', 'city_name', 'ZIP_code', 'country_code', 'budget', 'area', 'power_req')

class SiteAnalForm(forms.ModelForm):
    class Meta:
        model = SiteNames
        fields = ('site_name',)


