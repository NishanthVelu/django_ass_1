from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20)
    genre = models.CharField(max_length=50)
    description = models.TextField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=50)
    student_id = models.CharField(max_length=20)
    year = models.DateField()
    department = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name

class BorrowedBook(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.student.name} borrowed {self.book.title}"