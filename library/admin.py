from django.contrib import admin
from .models import Book, Author, Bookingbook, Commit
from import_export.admin import ImportExportModelAdmin


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "birth_data")
    search_fields = ("first_name",)#first_name buuyicha qidiradi


@admin.register(Book)
class Bookadmin(ImportExportModelAdmin):
    list_display = ("id", "title", "description_20", "price", "cound", "author", "comment_count", "create_data")
    list_display_links = ("id", "title", "description_20", "price", "cound", "author", "comment_count", "create_data")
    search_fields = ("id", "title") #id va title buyicha qidishda ishlatiladi
    ordering = ("title", )#  title buyicha tartiblaydi
    autocomplete_fields = ("author",)

    def description_20(self, obj):
        return obj.description[:20]

    def comment_count(self, obj):
        return obj.comment.all().count()

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