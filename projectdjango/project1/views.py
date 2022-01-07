from django.shortcuts import render
from django.http import HttpResponse
from googletrans import Translator


def home(request):
    return render (request, 'home.html')
# Create your views here.

def translate(request):
    return render(request,'translate.html')


def trans(request):
    ti = request.GET["text"]
    translater = Translator()
    out=translater.translate(ti,dest="en")
    return render(request,'answer.html',{'texty': out.text })
