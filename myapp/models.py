from django.db import models


# Create your models here.


class employee(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.CharField(max_length=50,default="0")
    password = models.CharField(max_length=20,default="0")
    usertype = models.CharField(max_length=20,default="0")


class Property(models.Model):
    propertyImages1 = models.FileField(upload_to='images1')
    propertyImages2 = models.FileField(upload_to='images2')
    propertyImages3 = models.FileField(upload_to='images3')
    propertyDescription = models.CharField(max_length=500)
    propertyArea = models.CharField(max_length=20)
    propertyBeds = models.IntegerField(max_length=10)
    propertyBaths = models.IntegerField(max_length=10)
    propertyGarages = models.IntegerField(max_length=10)
    propertyPrice = models.IntegerField(max_length=10)
    propertyLocation = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin = models.CharField(max_length=10)
    contactDetails = models.IntegerField(max_length=20)
    bhkType = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
