from django.db import models

# Create your models here.
class FileModel(models.Model):
      number = models.AutoField(primary_key = True)
      name = models.CharField(max_length=100,null=False)
      file = models.FileField(upload_to='my_Documents/')

