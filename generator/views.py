from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render (request, 'home.html', {})

def pwdgen(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    password = ''

    length  = int(request.GET.get('length'))

    if(request.GET.get('uppercase')):
        characters.extend('ABCDEFGHIJKLMNOPQRST')

    for i in range(length):
        password += random.choice(characters)

    return render(request, 'password.html', {'password': password})