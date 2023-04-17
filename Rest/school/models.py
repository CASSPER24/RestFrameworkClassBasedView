from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=25)
    student_id = models.CharField(max_length=10)
    stud_class = models.CharField(max_length=2)
    age = models.IntegerField()
    email = models.EmailField(max_length=35)
    phone = models.CharField(max_length=13)



class Teacher(models.Model):
    name = models.CharField(max_length=25)
    teacher_id = models.CharField(max_length=10)
    subject = models.CharField(max_length=10)
    age = models.IntegerField()
    email = models.EmailField(max_length=35)
    phone = models.CharField(max_length=13)