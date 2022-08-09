from django.db import models
# Create your models here.
class Team(models.Model):
    tname=models.CharField(max_length=200)
    def __str__(self):
        return self.tname
class Player(models.Model):
    pname=models.CharField(max_length=255)
    team=models.ForeignKey(Team,on_delete=models.CASCADE,)
    def __str__(self):
        return self.pname