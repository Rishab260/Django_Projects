from django.shortcuts import render
from WebApp.models import Emp
# Create your views here.
def EmpView(request):
    EmpList=Emp.objects.all()
    MyDict={'elist':EmpList}
    return render(request,'MyApp/welcome.html',MyDict)