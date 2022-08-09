from django.shortcuts import render
# Create your views here.
def MyTempView(request):
    return render(request,'MyApp/welcome.html')
