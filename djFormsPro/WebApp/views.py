from django.shortcuts import render
from WebApp import forms
# Create your views here.
def EmpFrontView(request):
    form=forms.EmpForms()
    return render(request,'MyApp/welcome.html',{'form':form})