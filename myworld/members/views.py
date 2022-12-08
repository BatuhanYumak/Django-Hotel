from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
 
def hotel (request):
  return render(request, 'hotel.html')

def amsterdam(request):
      return render(request, 'amsterdam.html')
    

 