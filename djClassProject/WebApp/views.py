from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.
# class CBV(View):
#     def get(self,request):
#         return HttpResponse("<h1>Welcome to Class Based Get Views...!!</h1>")
#     def post(self,request):
#         return HttpResponse("Hello Post Method....!!")
def Hello(request):
    if request.method=='POST':
        return HttpResponse("Welcome to FBV....!!!")
    else:
        return HttpResponse("Hey Thank U....!!")
