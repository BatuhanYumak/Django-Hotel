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