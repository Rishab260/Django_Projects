from django.shortcuts import render
from WebApp.models import FilterModel
# Create your views here.
def DataView(request):
    datalist=FilterModel.objects.all()
    return render(request,'MyApp/welcome.html',{'datalist':datalist})

def UviewData(request):
    datalist=FilterModel.objects.all()
    return render(request, 'MyApp/upper.html', {'datalist': datalist})


def LviewData(request):
    datalist=FilterModel.objects.all()
    return render(request, 'MyApp/lower.html', {'datalist': datalist})

def CviewData(request):
    datalist=FilterModel.objects.all()
    return render(request, 'MyApp/ctf.html', {'datalist': datalist})