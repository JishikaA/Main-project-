from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import ForeignKey, DO_NOTHING


# Create your models here.
class Login(AbstractUser):
    is_Donor =models.BooleanField(default=False)
    is_Receiver =models.BooleanField(default=False)

class Donor(models.Model):
    user =models.OneToOneField(Login,on_delete=models.CASCADE,related_name='Donor')
    name =models.CharField(max_length=20)
    age =models.CharField(max_length=2)
    DOB =models.DateField()
    address =models.CharField(max_length=50)
    phone_number =models.CharField(max_length=10)
    email =models.EmailField()
    BLOOD_GROUP = (
        ('A+', 'A+'),
        ('A -', 'A -'),
        ('B +','B +'),
        ('B-','B-'),
        ('AB+','AB+'),
        ('AB-','AB-'),
        ('O+','O+'),
        ('O-','O-')
    )
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP)
    profile = models.FileField(upload_to='profile/')

class Receiver(models.Model):
    user =models.OneToOneField(Login,on_delete=models.CASCADE,related_name='Receiver')
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=2)
    DOB = models.DateField()
    blood_group = models.CharField(max_length=5)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    BLOOD_GROUP = (
        ('A+', 'A+'),
        ('A -', 'A -'),
        ('B +', 'B +'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-')
    )
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP)
    profile = models.FileField(upload_to='document/')

class Receiver_Request(models.Model):
    Receiver_name =models.ForeignKey('Receiver',on_delete=models.CASCADE)
    Donor_name =ForeignKey('Donor',on_delete=DO_NOTHING,blank=True,null=True)
    date =models.DateField()
    BLOOD_GROUP = (
        ('A+', 'A+'),
        ('A -', 'A -'),
        ('B +', 'B +'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-')
    )
    blood_groups =models.CharField(max_length=3,choices=BLOOD_GROUP)
    Hospital_name =models.CharField(max_length=50)
    place =models.CharField(max_length=50)
    contact =models.CharField(max_length=10)
    Status =models.IntegerField(default=0)

class Feedback(models.Model):
    Receiver_name =models.ForeignKey('receiver',on_delete=models.CASCADE)
    message =models.TextField()
    date =models.DateField(auto_now=True)
    Replay =models.CharField(max_length=200,null=True,blank=True)