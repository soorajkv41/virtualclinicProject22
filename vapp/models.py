from django.db import models

# Create your models here.
class appointmntdb(models.Model):
    hospitalname=models.CharField(max_length=100,null=True,blank=True)
    Department=models.CharField(max_length=100,null=True,blank=True)
    Doctors=models.CharField(max_length=100,null=True,blank=True)
    Date=models.DateField(null=True,blank=True)
    time=models.TimeField(null=True,blank=True)
    Name=models.CharField(max_length=100,null=True,blank=True)
    phonenum=models.IntegerField(null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    Message=models.CharField(max_length=1000,null=True,blank=True)
class contactdb(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    emailadd=models.EmailField(null=True,blank=True)
    query=models.CharField(max_length=100,null=True,blank=True)
    phnnum=models.IntegerField(null=True,blank=True)
    message=models.CharField(max_length=1000,null=True,blank=True)
# class cartdb(models.Model):
#     Medicinename=models.CharField(max_length=100,null=True,blank=True)
#     price=models.IntegerField(null=True,blank=True)
#     description=models.CharField(max_length=1000,null=True,blank=True)
#     qty=models.IntegerField(null=True,blank=True)
#     totalprice=models.IntegerField(null=True,blank=True)
class registerdb(models.Model):
    firstname=models.CharField(max_length=100,null=True,blank=True)
    lastname=models.CharField(max_length=100,null=True,blank=True)
    dateofbirth=models.DateField(null=True,blank=True)
    gender=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    number=models.IntegerField(null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    repeatpassword=models.CharField(max_length=100,null=True,blank=True)
class servicebookdb(models.Model):
    servicename=models.CharField(max_length=100,null=True,blank=True)
    date=models.DateField(null=True,blank=True)
    time=models.TimeField(null=True,blank=True)
    fullname=models.CharField(null=True,blank=True,max_length=100)
    phone=models.IntegerField(null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    message=models.CharField(max_length=1000,null=True,blank=True)
class disappdb(models.Model):
    hospitalname=models.CharField(max_length=100,null=True,blank=True)
    doctorname=models.CharField(max_length=100,null=True,blank=True)
    date=models.DateField(null=True,blank=True)
    Time=models.TimeField(null=True,blank=True)
    email=models.EmailField(null=True,blank=True)

