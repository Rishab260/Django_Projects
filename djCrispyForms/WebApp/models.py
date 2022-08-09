from django.db import models
# Create your models here.
class Person(models.Model):
    Name=models.CharField(max_length=300)
    Email=models.EmailField(blank=True)
    JobTitle=models.CharField(max_length=300,blank=True)
    Biodata=models.TextField(blank=True)