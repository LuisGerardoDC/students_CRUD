from django.shortcuts import render

# Create your views here.
def login(request):
    """ log in screen"""
    return render(request,'login.html')

def sign_up(request):
    """ log in screen"""
    return render(request,'sign_up.html')