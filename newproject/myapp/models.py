from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pictures')
    # image2=models.ImageField(upload_to='pictures')
    description=models.TextField()

    def __str__(self):
        return self.name

class Meettheteam(models.Model):
    teamname=models.CharField(max_length=250)
    teamimage=models.ImageField(upload_to='pictures')
    bio=models.TextField()

    def __str__(self):
        return self.teamname

class Symbol(models.Model):
    symimage=models.ImageField(upload_to='pictures')


