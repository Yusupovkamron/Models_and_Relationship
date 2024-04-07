from django.shortcuts import render, redirect
from django.views import View
from .models import Book
# from .forms import AddBookModleForm
from django.http import HttpResponse

class BooksListView(View):
    def get(self, request):
        search=request.GET.get("search")
        books = Book.objects.all(title__icontains=search)
        if not books:
            return HttpResponse("NOT FOUND")
        else:
            context = {
                "books": book,
                "search": search
            }
        return render(request, "library.html", context)

class BookDetailView(View):
    def get(self, requesst, id):
        book = Book.objects.get(id=id)
        return render(requesst, "book_detail.html", {"book": book})