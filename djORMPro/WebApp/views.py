from django.shortcuts import render
from WebApp.models import Student
# Create your views here.
def Display(request):
    stds=Student.objects.filter(stdmarks__gte=30)
    print(type(stds))
    PyStds={'stds':stds}
    return render(request,'MyApp/index.html',PyStds)