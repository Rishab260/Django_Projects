from django.shortcuts import render
import datetime
# Create your views here.
def DataView(request):
    dt=datetime.datetime.now()
    name="PYTHON Django Web Framework.!"
    dic={'dt':dt,'name':name}
    return render(request,'MyApp/welcome.html',dic)