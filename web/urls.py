from django.urls import path
from . import views
urlpatterns = [
    path('Hello', views.HELLO, name='HELLO'),
    path('', views.Home, name='Home'),
    path('Login_page.html', views.Login, name='Login'),
    path('Sign_in_page.html', views.Sign_in, name='Sign_in')

]