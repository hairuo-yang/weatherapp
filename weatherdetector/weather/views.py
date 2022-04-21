from django.shortcuts import render
import json
import urllib.request
# Create your views here.



def index(request):
    if request.method=='POST':
        city=request.POST['city']
        res=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=8e5a93cdb68875f209560863f214fb12').read()
        json_data=json.loads(res)
        data={
            'country_code': str(json_data['sys']['country']),
            'city': str(json_data['name']),
            'coordinate': str(json_data['coord']['lon'])+', '+str(json_data['coord']['lat']),
            'temp': str(json_data['main']['temp'])+' Kelvin',
            'pressure': str(json_data['main']['pressure'])+' mb',
            'humidity': str(json_data['main']['humidity'])+' %',
        }

    else: 
        data={}
    return render(request, 'index.html', data)