from django.urls import path
from .views import student_views

urlpatterns = [
    path("student/", student_views),
]