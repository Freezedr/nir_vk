from django.shortcuts import render
from urllib.request import urlopen
from json import loads

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect, HttpRequest

# VK App settings
VK_APP_ID = '4866026'
VK_APP_SECRET = '7byri06kTN3nhckyICfU'
access_token = ''

def start_auth(request):
    vk_authorize_url = 'https://oauth.vk.com/authorize?' + \
                   'client_id=' + VK_APP_ID + \
                   '&display=page' + \
                   '&redirect_uri=http://qazwsxe.ru:8000/login_vk/callback' + \
                   '&scope=audio,offline' + \
                   '&response_type=code'

    return HttpResponseRedirect(vk_authorize_url)

def getting_code(request):
    code = request.GET["code"]
    redirect_url = "https://oauth.vk.com/access_token?" + \
               "client_id=" + VK_APP_ID + \
               "&client_secret=" + VK_APP_SECRET + \
               "&redirect_uri=http://qazwsxe.ru:8000/login_vk/callback" + \
               "&code=" + code
    redirect = urlopen(redirect_url)
    result = loads(redirect.read().decode('utf-8'))
    access_token = result['access_token']
    f = open('access_token.txt', 'w')
    f.write(access_token)
    return HttpResponse('Access token: '+access_token)