from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.contrib.auth.models import User
from pprint import pprint
from .forms import UserForm

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
# Hier haal ik data uit de database en vervolgens dat te displayen op mijn gewenste pagina


def hotel(request):
    return render(request, 'hotel.html')


def amsterdam(request):
    context = {
        'amsterdam': Informatie.objects.filter(city_name='Amsterdam')
    }
    return render(request, 'amsterdam.html', context)


def antwerpen(request):
    context = {
        'antwerpen': Informatie.objects.filter(city_name='Antwerpen')
    }
    return render(request, 'antwerpen.html', context)


def athene(request):
    context = {
        'athene': Informatie.objects.filter(city_name='Athene')
    }
    return render(request, 'athene.html', context)


def bangkok(request):
    context = {
        'bangkok': Informatie.objects.filter(city_name='Bangkok')
    }
    return render(request, 'bangkok.html', context)


def barcelona(request):
    context = {
        'barcelona': Informatie.objects.filter(city_name='Barcelona')
    }
    return render(request, 'barcelona.html', context)


def berlijn(request):
    context = {
        'berlijn': Informatie.objects.filter(city_name='Berlijn')
    }
    return render(request, 'berlijn.html', context)


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'login.html')

from django.contrib.auth import login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
 
 
 
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'inlog.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'inlog.html')
# Registratie pagina back-end
def signup_view(request):

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})