from django.shortcuts import render
from WebApp.models import Driver
# Create your views here.
def DList(request):
    items=Driver.objects.all()
    return render(request,'MyApp/Many.html',{'items':items})