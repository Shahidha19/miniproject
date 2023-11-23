from django.db import models
from django.contrib.auth.models import User
# Create your models here.
'''class Complaint(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    complaint = models.TextField()

    def __str__(self):
        return self.name'''

class ComplaintSystem(models.Model):
    username=models.CharField(max_length=50, null=True, blank=True)
    regno = models.CharField(max_length=100, null=True, blank=True)
    dept = models.CharField(max_length=100, null=True, blank=True)
    complaint = models.CharField(max_length=1000, null=True, blank=True)
    status = models.CharField(max_length=1000, null=True, blank=True)
    def __str__(self):
        return self.dept



