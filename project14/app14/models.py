from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=30)
    contact_no = models.IntegerField(unique=True)
    email = models.EmailField(max_length=30,unique=True)
    password = models.CharField(max_length=10,null=False)
    location = models.CharField(max_length=30,null=False)
    photo = models.ImageField(upload_to='student_images',null=False)
    dob = models.DateField()
    date_of_reg = models.DateField(auto_now_add=True)


