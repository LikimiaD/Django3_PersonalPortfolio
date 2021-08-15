from django.db import models
from datetime import date

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=100)
    small_desription = models.CharField(max_length=200)
    full_desription = models.CharField(max_length=1000, default='')
    date = models.DateField(default=date.today)