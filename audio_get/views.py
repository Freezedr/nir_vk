from django.shortcuts import render
from django.http import HttpResponseRedirect
from urllib.request import urlopen
from json import loads

# Create your views here.

def get_user_audio(request):
	f_acc = open('access_token.txt')
	access_token = f_acc.read()
	owner_id = '9111789' 
	url = 'https://api.vk.com/method/audio.get?' + \
          'owner_id=' + owner_id + \
          '&access_token=' + access_token
    redirect = urlopen(url)
    result = loads(redirect.read().decode('utf-8'))
    f = open('audio.txt', 'w')
    for item in result:
    	f.write(item)
    	
	return HttpResponseRedirect(url)