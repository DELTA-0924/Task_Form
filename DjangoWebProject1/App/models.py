
from django.db import models
from phonenumber_field.modelfields import PhoneNumber
from utilities.readyValues import *
from django_countries.fields import CountryField
class Profile(models.Model):
    id=models.AutoField(primary_key=True)
    Kyrgyz_som = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    USD = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    Euro = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    # Rest of your model fields...

    email=models.EmailField(blank=False,null=False)
    Confirm_Email=models.EmailField(blank=False,null=False) 
    First_name=models.CharField(max_length=20,blank=False,null=False)
    Last_name=models.CharField(max_length=40,blank=False,null=False)
    Phone_number=PhoneNumber()
    Connection=models.CharField(max_length=50,choices=ReadyConnetions,blank=True,null=True)
    Fund=models.CharField(max_length=60,choices=ReadyFundPriories,blank=True,null=True)
    Country = CountryField(blank_label='Select Country', blank=True, null=True)
    Inspired=models.TextField(max_length=200,blank=True,null=True)
    Comment=models.TextField(max_length=100,blank=True,null=True)
    Public_offer=models.BooleanField(default=False)