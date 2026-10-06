from django.db import models

# Create your models here.

#create table tablename(column1 type,colum2 type,....) #table definition


#table definition
class Person(models.Model):
    #id=models.IntegerField()
    name=models.CharField(max_length=20,primary_key=True)
    age=models.IntegerField()
    place=models.CharField(max_length=20)


class Movie(models.Model):
    name=models.CharField(max_length=100)
    director=models.CharField(max_length=100)
    year=models.IntegerField()