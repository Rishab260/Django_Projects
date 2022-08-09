from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def HomePage(request):
    return HttpResponse('<a href="/hi">Hello</a>')
def MyView(request):
    return HttpResponseRedirect(reverse('Hai'))
def ByeView(request):
    return HttpResponse("Good Bye...!!")
