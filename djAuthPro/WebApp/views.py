from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def HomePage(request):
    return render(request,'MyApp/home.html')

@login_required
def CustPage(request):
    return render(request,'MyApp/customer.html')

def Logout(request):
    return render(request,'MyApp/logout.html')