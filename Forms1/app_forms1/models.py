from django.db import models

class EmployeeRegistrationModel(models.Model):
    number = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100,null=False)
    contact = models.IntegerField(unique=True)
    salary = models.FloatField(null=False)
    designation = models.CharField(max_length=100,null=False)
    dob = models.DateField(null=False,default='2001-01-01')
    #email = models.EmailField(null=False,max_length=100,default="xxxxxx@gmail.com")
    email = models.EmailField(null=False,max_length=100,default="")