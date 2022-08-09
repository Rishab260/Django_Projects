from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse
# Create your views here.
class TempView(TemplateView):
    template_name = 'MyApp/Hello.html'
