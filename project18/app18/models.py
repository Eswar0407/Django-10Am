from django.db import models

class StudentDetailsModel(models.Model):
    number = models.AutoField(primary_key = True)
    name = models.CharField(max_length=30,null=False)
    contact = models.IntegerField(null=False,unique=True)
    photo = models.ImageField(upload_to="student_images")
    dob = models.DateField()
    email = models.EmailField(max_length=30,unique=True)
    password = models.CharField(max_length=50,null=False)
    date_of_reg = models.DateField(auto_now_add=True)
