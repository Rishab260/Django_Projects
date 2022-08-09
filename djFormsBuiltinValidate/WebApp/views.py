from django.shortcuts import render
from WebApp import forms
from django.http import HttpResponseRedirect
# Create your views here.
def Thanks(request):
    return render(request,'MyApp/thanks.html')
def EmpView(request):
    if request.method == 'POST':
        form=forms.EmpForm(request.POST)
        if form.is_valid():
            print("Welcome to Validations....!!")
            print(form.cleaned_data['Name'])
            print(form.cleaned_data['Salary'])
            #print(form.cleaned_data['Opinion'])
            return HttpResponseRedirect('/thanks')
    else:
        form=forms.EmpForm()
    return render(request,'MyApp/welcome.html',{'form':form})