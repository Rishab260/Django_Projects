from django.shortcuts import render
# Create your views here.
def TemplateView(request):
    return render(request,'MyFile/welcome.html')