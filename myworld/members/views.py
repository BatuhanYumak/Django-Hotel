from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.urls import reverse


from django import forms
from django.contrib.auth.models import User


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


# login/logout en registratie pagina

def index(request):
    message = request.session.get('message', None)
    if message:
        del request.session['message']
    return render(request, 'index.html', {'message': message})

# Hier check hiij code of  het overeenkomt met de gebruiker zijn inglog gevens die opgeslagen is in het database


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['message'] = "You are logged in"
                return redirect('index')
            else:
                return render(request, 'login.html', {'error': 'Invalid credentials'})
        else:
            return render(request, 'login.html', {'error': 'Username and password are required'})
    else:
        return render(request, 'login.html')

# Hier verstuur de data van de gebruiker naar de database na dat hij/zij een account heef gemaakt word diegene verstuurd naar de login pagina


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# logout functie


def logout_view(request):
    logout(request)
    return render(request, 'index.html', {'message1': 'You are logged out'})

