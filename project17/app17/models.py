from django.db import models

class ProductModel(models.Model):
    number = models.AutoField(primary_key = True)
    name = models.CharField(max_length=30,null=False)
    price = models.FloatField(null=False)
    photo = models.ImageField(upload_to='product_images/')



