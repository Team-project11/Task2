from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from pprint import pprint

# Create your views here.
def ProfileData(request,User_id):
    url = "http://127.0.0.1:8000/Json_Data"
    Response = requests.get(url)
    print(Response.text)
    return render(request,'userpage.html')
def Admin_Post(request):
    url = "http://127.0.0.1:8000/RestApi/?search={}&"
    headers = {'Authorization': 'Token 5d27228a4a22bb7125dcf2b5fe2df020c424c040'}
    city = request.GET.get('city')
    r = requests.get(url.format(city),headers=headers).json()
    pprint(r)
    
    adminpost={
            '': city,
            'Description' : r[0]['Description'],
            'Icon': r[0]['Icon'],
            'Temperature':r[0]['Temperature'],
            'Country' : r[0]['Country'],
            }
    

    context = {'weather':weather}
    return render(request,'weather1.html',context)
    
