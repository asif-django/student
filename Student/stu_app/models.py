from django.db import models

# Create your models here.

class Student_info(models.Model):
     name = models.CharField(max_length=100)
     age = models.IntegerField()
     email = models.EmailField()
     photo = models.ImageField(upload_to="images/")
     nationality = models.CharField(max_length=100)