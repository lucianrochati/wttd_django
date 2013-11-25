#coding: utf8-8
from django.http import HttpResponse

def home(request):
    return HttpResponse('Bem vindo ao Eventex')



# Create your views here.
