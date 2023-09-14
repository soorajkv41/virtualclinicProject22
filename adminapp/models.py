from django.db import models

# Create your models here.
class hospitaldb(models.Model):
    hospitalname=models.CharField(null=True,max_length=100,blank=True)
    hospitalcode=models.CharField(null=True,max_length=100,blank=True)
    contactno=models.CharField(null=True,max_length=100,blank=True)
    email=models.EmailField(null=True,blank=True,max_length=100)
    address1=models.CharField(null=True,max_length=500,blank=True)
    addrress2=models.CharField(null=True,blank=True,max_length=500)
    state=models.CharField(null=True,blank=True,max_length=100)
    district=models.CharField(null=True,blank=True,max_length=100)
    pincode=models.IntegerField(null=True,blank=True)
class doctordb(models.Model):
    hospitalname=models.CharField(null=True,blank=True,max_length=100)
    doctorname=models.CharField(null=True,blank=True,max_length=100)
    department=models.CharField(null=True,blank=True,max_length=100)
    contactnumber=models.IntegerField(null=True,blank=True)
    Email=models.EmailField(null=True,blank=True)
    description=models.CharField(max_length=1000,null=True,blank=True)
    Doctor_photo=models.ImageField(upload_to="photos",null=True,blank=True)
class servicedb(models.Model):
    servicename=models.CharField(null=True,blank=True,max_length=100)
    rates=models.IntegerField(null=True,blank=True)
    description=models.CharField(max_length=1000,null=True,blank=True)
    serv_photo=models.ImageField(upload_to="pic",null=True,blank=True)
class medicinedb(models.Model):
    medicinename=models.CharField(null=True,blank=True,max_length=100)
    companyname=models.CharField(null=True,blank=True,max_length=100)
    price=models.IntegerField(null=True,blank=True)
    description=models.CharField(null=True,blank=True,max_length=1000)
    photo=models.ImageField(upload_to="pic",null=True,blank=True)
class gallerydb(models.Model):
    photoshortname=models.CharField(max_length=100,null=True,blank=True)
    description=models.CharField(max_length=1000,null=True,blank=True)
    photo=models.ImageField(upload_to="pic",null=True,blank=True)
class deptdb(models.Model):
    deptname=models.CharField(max_length=100,null=True,blank=True)
    description=models.CharField(max_length=1000,null=True,blank=True)
    description2=models.CharField(max_length=1000,null=True,blank=True)
    deptphoto= models.ImageField(upload_to="pic", null=True, blank=True)
    feature1=models.CharField(max_length=100,null=True,blank=True)
    feature2=models.CharField(max_length=100,null=True,blank=True)
    features3=models.CharField(max_length=100,null=True,blank=True)
    features4=models.CharField(max_length=100,null=True,blank=True)
class savedeldb(models.Model):
    servicename=models.CharField(max_length=100,null=True,blank=True)
    date=models.CharField(max_length=100,null=True,blank=True)
    time=models.CharField(max_length=100,null=True,blank=True)
    patientname=models.CharField(max_length=100,null=True,blank=True)
    Mobilenumber=models.IntegerField(null=True,blank=True)
    emailid=models.EmailField(null=True,blank=True)
    remarks=models.CharField(max_length=1000,null=True,blank=True)

class savedelappointmentdb(models.Model):
    Hospitalname=models.CharField(max_length=100,null=True,blank=True)
    DoctorName=models.CharField(max_length=100,null=True,blank=True)
    Department=models.CharField(max_length=100,null=True,blank=True)
    Date=models.CharField(max_length=100,null=True,blank=True)
    Time=models.CharField(max_length=100,null=True,blank=True)
    patientname=models.CharField(max_length=100,null=True,blank=True)
    phonenumber=models.IntegerField(null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    remarks=models.CharField(max_length=1000,null=True,blank=True)

