from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse
# Create your views here.
class TempView(View):
    def get(self,request):
        return HttpResponse("<h1>Welcome to Class Based Views...!!</h1>")

class TempCBV(TemplateView):
    template_name='MyApp/hello.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['EmpName']='SARA THOMUS'
        context['EmpLocation']='CHENNAI'
        context['EmpSalary']='$1000000'
        return context

#Model ==> Backend
#Forms ==> FrontEnd
#ModelForms ==> Frontend -Backend