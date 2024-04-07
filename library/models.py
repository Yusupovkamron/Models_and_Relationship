from django.db import models
from student.models import Student



class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_data = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{self.id} {self.first_name} {self.last_name}"



class Commit(models.Model):
    text = models.TextField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    price = models.FloatField
    comment = models.ManyToManyField(Commit)
    cound = models.IntegerField(default=1)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    create_data = models.DateTimeField(auto_created=True)
    # autocomplete_fields = ("author", )



    def __str__(self):
        return f"{self.title} {self.price} {self.cound}"



class Bookingbook(models.Model):
    student = models.ManyToManyField(Student)
    Book = models.ManyToManyField(Book)
    take_data = models.DateTimeField(auto_now_add=True)
    returned_data = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} {self.Book}"


