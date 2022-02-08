from unicodedata import name
from django.db import models

class Job(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    department = models.CharField(max_length=100, blank = True, null = True)
    deadline = models.DateField()
    location = models.CharField(max_length=100)
    international = models.BooleanField()
    eligibility = models.CharField(max_length=100)
    major = models.CharField(max_length=100, blank = True, null = True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name