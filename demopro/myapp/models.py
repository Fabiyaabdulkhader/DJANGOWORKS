from django.db import models

# Create your models here.
class Student(models.Model):
    rollnumber=models.IntegerField()
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    place=models.CharField(max_length=20)
    marks=models.IntegerField()
