from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
 
def hotel (request):
  return render(request, 'hotel.html')

def amsterdam(request):
    context = {
     'amsterdam': Informatie.objects.filter(city_name = 'Amsterdam')
}
    return render(request, 'amsterdam.html', context)
  
def antwerpen(request):
    context = {
     'antwerpen': Informatie.objects.filter(city_name = 'Antwerpen')
}
    return render(request, 'antwerpen.html', context)
  
    
def athene(request):
    context = {
     'athene': Informatie.objects.filter(city_name = 'Athene')
}
    return render(request, 'athene.html', context)
  
def bangkok(request):
    context = {
     'bangkok': Informatie.objects.filter(city_name = 'Bangkok')
}
    return render(request, 'bangkok.html', context)
  
def barcelona(request):
    context = {
     'barcelona': Informatie.objects.filter(city_name = 'Barcelona')
}
    return render(request, 'barcelona.html', context)    

def berlijn(request):
    context = {
     'berlijn': Informatie.objects.filter(city_name = 'Berlijn')
}
    return render(request, 'berlijn.html', context)  
