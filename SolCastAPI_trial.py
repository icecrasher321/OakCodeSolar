import requests
api_address = "http://api.openweathermap.org/data/2.5/weather?appid=9222bd13d1d41b7034de04caf9991346&zip="
code = raw_input("Zip code followed by country code: ")
area = int(raw_input("Required area: "))
budget = raw_input("Budget: ")
url = api_address + code
json_data = requests.get(url).json()

lat = json_data[u'coord'][u'lat']
long = json_data[u'coord'][u'lon']

#all in /m^2 and rounded up - would be retrieved from a database of solar panels
LG_price = 250
LG_power = 192
cap = area*LG_power
final_price = area*LG_price

if(final_price<=budget):
   FP = final_price

else:
   print("The price for the installation has exceeded your budget")


api_address = "https://api.solcast.com.au/pv_power/estimated_actuals?longitude="+str(long)+"&latitude="+str(lat)+"&capacity="+str(cap)+"&api_key=YzazDu3g5WOIg7aDidudsx7n692SCV3N&format=json"
json_data = requests.get(api_address).json()
PV_Estimate = json_data['estimated_actuals'][0]['pv_estimate']
print (PV_Estimate, FP)
