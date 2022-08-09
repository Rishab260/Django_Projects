from django.shortcuts import render
from datetime import datetime
# Create your views here.
def TimeInfo(request):
    dt=datetime.now()
    name="Naresh i Technologies"
    th=int(dt.strftime('%H'))
    if th<12:
        wish='Good Morning Guys...!!'
    elif th<16:
        wish='Good Noon...!!'
    else:
        wish="Good Evening..!!"
    PyDict={'dt':dt,'name':name,'wish':wish}
    return render(request,'MyApp/welcome.html',context=PyDict)