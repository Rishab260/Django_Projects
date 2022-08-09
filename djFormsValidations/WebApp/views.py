from django.shortcuts import render
from WebApp import forms
from django.http import HttpResponseRedirect
# Create your views here.
def StudentView(request):
    if request.method=='POST':
        form=forms.StdForm(request.POST)
        if form.is_valid():
            print("Welcome Django Validations...!!")
            print(form.cleaned_data['SName'])
            print(form.cleaned_data['SFee'])
            print(form.cleaned_data['SLoc'])
            print(form.cleaned_data['SRes'])
            print(form.cleaned_data['SGrd'])
            return HttpResponseRedirect('/thanks')
    else:
        form=forms.StdForm()
    return render(request,'MyApp/welcome.html',{'form':form})

def Thanks(request):
    return render(request,'MyApp/thanks.html')