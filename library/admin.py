from django.contrib import admin
from .models import book, Author, Bookingbook, Commit
from import_export.admin import ImportExportModelAdmin


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "birth_data")


@admin.register(book)
class Bookadmin(ImportExportModelAdmin):
    list_display = ("id", "title", "description", "price", "cound", "author", "create_data")
    list_display_links = ("id", "title", "description", "price", "cound", "author", "create_data")
    search_fields = ("id", "title") #id va title buyicha qidishda ishlatiladi
    ordering = ("title", )#  title buyicha tartiblaydi

@admin.register(Bookingbook)
class Bookingbookadmin(admin.ModelAdmin):
    list_display = ("id", "student", "Book", "take_data", "returned_data")


    def student(self):
        return self.count()

    def Book(self):
        return self.count()




@admin.register(Commit)
class Commitadmin(admin.ModelAdmin):
    list_display = ("id", "text", "student")


# admin.site.register(Author)
# admin.site.register(Bookingbook)
# admin.site.register(Commit)