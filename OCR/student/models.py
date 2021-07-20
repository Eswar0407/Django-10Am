from django.db import models

class RegistrationModel(models.Model):
    Name = models.CharField(max_length=100,null=False)
    Contact = models.IntegerField(unique=True,null=False)
    Email = models.EmailField(max_length=100,unique=True,null=False)
    Password = models.CharField(max_length=100,null=False)
    Otp = models.IntegerField(null=False,default=0000)
    Status = models.CharField(max_length=30,null=False,default="pending")
    datetime = models.DateTimeField(auto_now_add=True)