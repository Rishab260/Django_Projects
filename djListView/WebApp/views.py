from django.shortcuts import render
from WebApp.models import Courses
from django.views.generic import ListView
# Create your views here.
class CourseListView(ListView):
    template_name='MyApp/CList.html'
    context_object_name='courses'
    model=Courses