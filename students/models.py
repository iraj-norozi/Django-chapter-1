from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    age = models.IntegerField()
    objects = models.Manager()
    def __str__(self):
        return self.name