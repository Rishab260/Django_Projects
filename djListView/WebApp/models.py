from django.db import models
# Create your models here.
class Courses(models.Model):
    Name=models.CharField(max_length=30)
    Trainer=models.CharField(max_length=40)
    Location=models.CharField(max_length=50)
    Days=models.IntegerField()