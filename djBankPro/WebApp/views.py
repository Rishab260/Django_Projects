from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def HomePage(request):
    return HttpResponse("Welcome to Django World..!!")
def IndexPage(request):
    return HttpResponse('Welcome to Index Page...!!')
def ByePage(request):
    return HttpResponse("<h1 style='color:red'>Welcome to Good Bye Page...!!</h1>")