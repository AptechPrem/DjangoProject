from django.db import models

from django.contrib.auth.models import *


class userAccount(models.Model):
    firstName=models.CharField(max_length=25)
    lastName=models.CharField(max_length=25)
    emailAddress=models.EmailField(max_length=25)
    password=models.CharField(max_length=25)
    

    def __str__(self):
        return self.firstName
    
class productDetails(models.Model):
    productName=models.CharField(max_length=25)
    productQty=models.IntegerField()
    productPrice=models.FloatField()
    productTotal=models.IntegerField()
    productDesc=models.CharField(max_length=25)
    productImage=models.ImageField(upload_to="uploads",null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.productName



class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    




