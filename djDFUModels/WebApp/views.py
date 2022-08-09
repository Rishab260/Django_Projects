from django.shortcuts import render
from django.http import HttpResponseRedirect
from WebApp.forms import StdForm
# Create your views here.
def Add(request):
    form=StdForm(request.POST, request.FILES)
    if form.is_valid():
        x=form.save()
        x.save()
        return HttpResponseRedirect('/')
    context={'form':form}
    return render(request,'MyApp/welcome.html',context)
def Home(request):
    return render(request,'MyApp/home.html')