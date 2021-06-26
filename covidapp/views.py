from django.shortcuts import render
import requests
import json
url = "https://covid-193.p.rapidapi.com/countries"

headers = {
    'x-rapidapi-key': "0338fa4e8fmsh7a8d784ce1c455ap1f4872jsn3773cfdbc376",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request ("GET", url, headers=headers).json()

# Create your views here.
def helloworldview(request):
    noofresults = (int(response['results']))
    mylist = []
    for x in range(0,noofresults):
        mylist.append(response['response'][x]['country'])
    context = {'mylist' : mylist }
    return render(request,'helloworld.html',context)