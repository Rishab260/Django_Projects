from django.shortcuts import render
# Create your views here.
def HomePage(request):
    return render(request,'MyApp/home.html')
def CoursePage(request):
    return render(request,'MyApp/course.html')
def SportsPage(request):
    return render(request,'MyApp/sports.html')
def NewsPage(request):
    return render(request,'MyApp/news.html')