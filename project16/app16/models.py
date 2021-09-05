from django.db import models

class EmployyeModel(models.Model):
    Idno = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    Salary = models.FloatField(max_length=20)
