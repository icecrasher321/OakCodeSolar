
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import *
from django.views.generic import TemplateView
from .models import *
import requests
import csv
from django.db.models import Q
from oakfest.models import *



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



def redir(request):
    return redirect('/dashboard')

def logout(request):
    auth_logout(request)
    return render(request, 'logged_out.html')
def test(request):
    return render(request, 'test.html')

def site_analysis(request):

        if request.method == "POST":

            form = SiteAnalForm(request.POST)

            api_address = "http://api.openweathermap.org/data/2.5/weather?appid=9222bd13d1d41b7034de04caf9991346&zip="
            if form.is_valid():

                b = Site.objects.get(site_name = form.cleaned_data['site_name'].site_name)
                cc_l = b.country_code.lower()
                code = str(b.ZIP_code) + ',' + cc_l
                area = int(b.area)
                budget = b.budget
                name = b.site_name
                pr = int(b.power_req)



                url = api_address + code
                json_data = requests.get(url).json()

                lat = json_data[u'coord'][u'lat']
                long = json_data[u'coord'][u'lon']

                names = []
                prices = []
                powers = []
                with open('/Users/rohangupta/Desktop/SP_db1.csv', 'r') as db:
                    reader = csv.reader(db)
                    for row in reader:
                        if row[0] == "Name of Product":
                            continue
                        else:
                            names.append(row[0])
                            prices.append(row[1])
                            powers.append(row[2])

                def match_index(price, power):
                    price_diff = abs((float(price) * area) - budget)
                    power_diff = abs((float(power) * area) - pr)
                    final_diff = price_diff + power_diff
                    return final_diff

                diffs = []

                for x in range(0, len(names)):
                    final_diff = match_index(prices[x], powers[x])
                    diffs.append(final_diff)

                ids = []

                for x in range(0, len(diffs)):
                    ids.append(x)

                dictionary = dict(zip(ids, diffs))

                import operator
                sorted_dict = sorted(dictionary.items(), key=operator.itemgetter(1))

                m = Site.objects.filter(ZIP_code = b.ZIP_code).exclude(site_name = b.site_name)


                cap = float(powers[sorted_dict[0][0]]) * float(area)
                fp = float(prices[sorted_dict[0][0]]) * float(area)

                final_names = []

                for x in range(0, len(diffs)):
                    final_names.append((names[sorted_dict[x][0]]))

                api_address = "https://api.solcast.com.au/pv_power/estimated_actuals?longitude=" + str(long) + "&latitude=" + str(
                    lat) + "&capacity=" + str(cap) + "&api_key=YzazDu3g5WOIg7aDidudsx7n692SCV3N&format=json"
                json_data = requests.get(api_address).json()
                PV_Estimate = json_data['estimated_actuals'][0]['pv_estimate']

                # if(final_price<=budget) and (cap>=PV_Estimate):
                # FP = final_price   AQZop9;0/[\

                data = []

                final_data = {
                    'estimate': int(PV_Estimate),
                    'site_name': b.site_name,
                    'final_price': int(fp),
                    'final_order': final_names,
                    'matching_sites': m,
                }

                data.append(final_data)
                context = {'data': data, 'form': form}
                return render(request, 'site_anal.html', context)
            else:
                form = SiteAnalForm()
        else:
            form = SiteAnalForm()
            context = {'form':form}
            return render(request, 'site_anal.html', context)




