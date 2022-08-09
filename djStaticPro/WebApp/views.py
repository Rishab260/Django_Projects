from django.shortcuts import render
from datetime import datetime
# Create your views here.
def TimeInfo(request):
    dt=datetime.now()
    name='Naresh i Technologies'
    dic={'dt':dt,'name':name}
    return render(request,'MyApp/welcome.html',dic)