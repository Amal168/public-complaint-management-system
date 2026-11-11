from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Citizen(models.Model):
    photo=models.FileField()
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    mobile=models.CharField(max_length=10)
    dob=models.DateField()
    gender=models.CharField(max_length=10)
    place=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    pincode=models.IntegerField()
    LOGIN=models.OneToOneField(User,on_delete=models.CASCADE)

class Complaint(models.Model):
    complaints=models.CharField(max_length=200)
    replay=models.CharField(max_length=200)
    date=models.DateTimeField()
    CITIZEN=models.ForeignKey(Citizen,on_delete=models.CASCADE)

