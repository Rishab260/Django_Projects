from django.shortcuts import render
from django.http import HttpResponseRedirect
from WebApp import forms
# Create your views here.
def EmpView(request):
    form=forms.EmpForm()
    if request.method == 'POST':
        form=forms.EmpForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("Data Inserted Successfully")
            return HttpResponseRedirect('/thanks')
    return render(request,'MyApp/welcome.html',{'form':form})

def Thanks(request):
    return render(request,'MyApp/thanks.html')