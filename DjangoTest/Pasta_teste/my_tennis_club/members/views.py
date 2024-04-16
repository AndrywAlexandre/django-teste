from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def members(request):
  #Criando conexão entre o arquivo MyFirst.html e o Views.py
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())



from .models import Member

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))