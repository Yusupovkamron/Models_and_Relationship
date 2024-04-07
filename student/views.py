from django.shortcuts import render
from django.views import View
from .models import Student



class StudentListView(View):
    def get(self, request):
        students = Student.objects.all()
        return render(request,  "student.html")


class landingview(View):
    def get(self, request):
        return render(request, "imndex.html")
