from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from .models import Company
from .forms import NewForm
# Create your views here.
def Home(request):
    orglist=Company.objects.all()
    return render(request,'MyApp/home.html',{'orglist':orglist})

def OrgCreate(request):
    form=NewForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        x=form.save()
        x.save()
        return HttpResponseRedirect('/')
    return render(request,'MyApp/create.html',{'form':form})

def OrgRetrive(request,id=None):
    x=get_object_or_404(Company,id=id)
    return render(request,'MyApp/retrive.html',{'x':x})

def OrgUpdate(request,id=None):
    instance=get_object_or_404(Company,id=id)
    form=NewForm(request.POST or None,request.FILES or None,instance=instance)
    if form.is_valid():
        instance=form.save()
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    return render(request,'MyApp/update.html',{'instance':instance,'form':form})