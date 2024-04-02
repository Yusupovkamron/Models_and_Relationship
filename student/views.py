
from django.shortcuts import render

def student_views(request):
    return render(request, "student.html")