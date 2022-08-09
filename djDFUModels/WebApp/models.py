from django.db import models
# Create your models here.
class Student(models.Model):
    Stdno=models.IntegerField()
    StdName=models.CharField(max_length=100)
    ProfPic=models.FileField(blank=True,null=True)
    StdAdd=models.CharField(max_length=50)