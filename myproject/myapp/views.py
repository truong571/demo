from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def members(request):
    return HttpResponse("Hello world!")

def my_view(request):
  template = loader.get_template('my_template.html')
  return HttpResponse(template.render())