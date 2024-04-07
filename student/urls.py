from django.urls import path
from .views import StudentListView, landingview

urlpatterns = [
    path("student/", StudentListView.as_view(), name="student"),
    path("", landingview.as_view(), name="landing"),
]