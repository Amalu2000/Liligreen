from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class Products(models.Model):
    name=models.CharField(max_length=100)
    img1=models.ImageField(upload_to='product_picture',null=True,blank=True)
    description=models.TextField()
    details=models.TextField(default=1)
    specification1=models.CharField(max_length=200)
    specification2=models.CharField(max_length=200)
    specification3=models.CharField(max_length=200)
    specification4=models.CharField(max_length=200)
    specification5=models.CharField(max_length=200)
    specification6=models.CharField(max_length=200)
    ctry = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    us=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name
    


class Review(models.Model):
    us=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE) 
    review=models.TextField(max_length=500,blank=True)
    rating=models.IntegerField(choices=[(i,i) for i in range(1,6)])
    created_at=models.DateField(auto_now_add=True)  

    def __str__ (self):
        return str(self.product)
    
    