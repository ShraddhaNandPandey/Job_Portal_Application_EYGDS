# jobs/models.py

from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    ...

class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    ...

class Applicant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    ...
