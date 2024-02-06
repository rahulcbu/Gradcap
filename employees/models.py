from django.db import models


# Create your models here.

class Student(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.first_name



