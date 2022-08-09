from django.db import models
# Create your models here.
class Student(models.Model):
    stdno=models.IntegerField()
    stdname=models.CharField(max_length=100)
    stdmarks=models.FloatField()
    stdresult=models.CharField(max_length=100)