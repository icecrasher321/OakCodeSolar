'''import os, sys
import requests
import csv

proj_path = '/Users/rohangupta/Desktop/oakfest'
# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oakfest.settings")
sys.path.append(proj_path)

# This is so my local_settings.py gets loaded.
os.chdir(proj_path)

# This is so models get loaded.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from oakfest.models import *


a = input("enter site name")
b = Site.objects.get(site_name = a)
cc_l = b.country_code.lower()
api_address = "http://api.openweathermap.org/data/2.5/weather?appid=9222bd13d1d41b7034de04caf9991346&zip="
code = str(b.ZIP_code) + ','+ cc_l
area = int (b.area)
budget = b.budget
pr = int(b.power_req)

#power_bill = int(raw_input("Power bill value: "))
url = api_address + code
json_data = requests.get(url).json()

lat = json_data[u'coord'][u'lat']
long = json_data[u'coord'][u'lon']

names = []
prices = []
powers = []
with open('/Users/rohangupta/Desktop/SP_db.csv','r') as db:
    reader = csv.reader(db)
    for row in reader:
        if row[0] == "Name of Product":
            continue
        else:
            names.append(row[0])
            prices.append(row[1])
            powers.append(row[2])


def match_index(price, power):
    price_diff = abs((float(price)*area)-budget)
    power_diff = abs((float(power)*area)-pr)
    final_diff = price_diff + power_diff
    return final_diff
diffs = []


for x in range(0,len(names)):
    final_diff = match_index(prices[x], powers[x])
    diffs.append(final_diff)


ids = []

for x in range(0, len(diffs)):
    ids.append(x)


dictionary = dict(zip(ids, diffs))
print(dictionary)


import operator
sorted_dict = sorted(dictionary.items(), key=operator.itemgetter(1))

print(sorted_dict)

cap = float(powers[sorted_dict[0][0]])*float(area)
fp = float(prices[sorted_dict[0][0]])*float(area)

final_names = []

for x in range(0, len(diffs)):
    final_names.append((names[sorted_dict[x][0]]))

api_address = "https://api.solcast.com.au/pv_power/estimated_actuals?longitude="+str(long)+"&latitude="+str(lat)+"&capacity="+str(cap)+"&api_key=YzazDu3g5WOIg7aDidudsx7n692SCV3N&format=json"
json_data = requests.get(api_address).json()
PV_Estimate = json_data['estimated_actuals'][0]['pv_estimate']

#if(final_price<=budget) and (cap>=PV_Estimate):
    #FP = final_price   AQZop9;0/[\

print (PV_Estimate, fp)
print (final_names)'''

