from django.shortcuts import render
from .models import Team
# Create your views here.
def TeamList(request):
    items=Team.objects.all()
    return render(request,'MyApp/Mone.html',{'items':items})