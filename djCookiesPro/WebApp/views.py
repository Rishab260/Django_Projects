from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def TestCookie(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>Welcome to Test Cookie..!!</h1>")
def CheckCookie(request):
    if request.session.test_cookie_worked():
        print("Hello Cookies are Working Fine...!!")
        request.session.delete_test_cookie()
        return HttpResponse("<h1>Cookies are Deleted Successfully..!!")