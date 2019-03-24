from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def HELLO(request):
    return HttpResponse('Hello World !!')


def Home(request):
    return render(request, 'Home_Page.html')


def Login(request):
    return render(request, 'Login_page.html')

def Sign_in(request):
    return render(request, 'Sign_in_page.html')


