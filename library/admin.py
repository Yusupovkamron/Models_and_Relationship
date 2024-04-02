from django.contrib import admin

from .models import book, Author, Bookingbook, Commit
admin.site.register(book)
admin.site.register(Author)
admin.site.register(Bookingbook)
admin.site.register(Commit)