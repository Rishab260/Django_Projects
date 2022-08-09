from django.db import models
# Create your models here.
class Employee(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=30)
    eloc=models.CharField(max_length=30)