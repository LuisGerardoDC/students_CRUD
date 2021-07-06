from django.shortcuts import render

# Create your views here.
def eval(request):
    """evaluation students"""
    return render(request,'eval.html')