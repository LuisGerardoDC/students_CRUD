from django.shortcuts import render

# Create your views here.
def students(request):
    """ CRUD students """
    return render(request,'crud_students.html')