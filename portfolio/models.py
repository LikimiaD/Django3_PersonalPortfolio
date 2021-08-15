from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Project(models.Model):
    title = models.CharField(max_length=100)
    desription = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    
class About(models.Model):
    title = models.CharField(max_length=100)
    desription = models.CharField(max_length=300)

class Skills_About(models.Model):
    title = models.CharField(max_length=100)
    desription = models.CharField(max_length=500)
    
class Skills_Value(models.Model):
    title = models.CharField(max_length=100)
    value = models.IntegerField(validators = [MinValueValidator(0), 
                                            MaxValueValidator(100)])