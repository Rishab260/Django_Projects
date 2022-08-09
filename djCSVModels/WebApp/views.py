from django.shortcuts import render
from django.http import HttpResponse
from WebApp.models import Employee
import csv
# Create your views here.
def GetFileCSV(request):
    x=HttpResponse(content_type='text/csv')
    x['Content-Disposition']='attachment;filename="MyData.csv"'
    y=Employee.objects.all()#All Records from that table
    z=csv.writer(x)
    for emp in y:
        z.writerow([emp.eid,emp.ename, emp.eloc])
    return x