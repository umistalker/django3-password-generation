import random

from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.

def home(reqest):
    return render(reqest, 'generator/home.html')

def password(reqest):

    characters = list('qwertyuiopasdfghjklzxcvbnm')

    if reqest.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    if reqest.GET.get('special'):
        characters.extend(list('!@#$%^&*()_'))
    if reqest.GET.get('numbers'):
        characters.extend(list('0123456789'))

    lenght = int(reqest.GET.get('length', 12))

    thepassword = ''


    for x in range(lenght):
        thepassword += random.choice(characters)
    return render(reqest, 'generator/password.html', {"password": thepassword})

def info(reqest):
    return render(reqest, 'generator/info.html')
