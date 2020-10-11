""" importing django model """
from django.db import models


# Create your models here.

class StudentInfo(models.Model):
    """here we are creating student information table"""
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    photo = models.ImageField(upload_to="images/")
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)
