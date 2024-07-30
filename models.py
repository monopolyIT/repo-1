from django.db import models
from datetime import *
# Create your models here.

class Employee(models.Model):
    EmployeeId=models.CharField(max_length=50,null=True,blank=False)
    EmpName=models.CharField(max_length=70,null=True,blank=False)
    EmpJoindate=models.DateTimeField(default=datetime.now(),null=True,blank=False)
    status=models.BooleanField(default=True,blank=False)
    