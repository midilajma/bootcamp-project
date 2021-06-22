import requests
#import os
from datetime import datetime
api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()
F3=open('k3.txt','w')
F3.close()
F3=open('k3.txt','a')
temp_city = ((api_data['main']['temp']) - 273.15)
F3.writelines(str(temp_city))
weather_desc = api_data['weather'][0]['description']
F3.writelines(str(weather_desc))
hmdt = api_data['main']['humidity']
F3.writelines(str(hmdt))
wind_spd = api_data['wind']['speed']
F3.writelines(str(wind_spd))
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
F3.writelines(str(date_time))
F3.close()
print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')+