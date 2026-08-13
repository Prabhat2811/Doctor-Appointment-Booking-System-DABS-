from django.db import models

# Create your models here.
class appointment(models.Model):
    name=models.CharField(max_length=50,default=0)
    email=models.EmailField(max_length=50,default=0)
    address=models.CharField(max_length=100,default=0)
    phone=models.IntegerField(default=0)
    age=models.IntegerField(default=0)
    option_gender=models.CharField(max_length=20,default=0)
    option_doctor=models.CharField(max_length=50,default=0)
    fee=models.CharField(max_length=10,default=0)
    date=models.CharField(max_length=50,default=0)
    time=models.CharField(max_length=50,default=0)
    reason=models.CharField(max_length=200000,default=0)
    doctor_pwd=models.CharField(max_length=50,default=123)
    class Meta:
        db_table="appointment"
        
class userdata(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    pwd=models.CharField(max_length=50)
    repwd=models.CharField(max_length=50)
    dob=models.CharField(max_length=50)
    chose1=models.CharField(max_length=50)
    class Meta:
        db_table="userdata"
        
class admin(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    pwd=models.CharField(max_length=50)
    repwd=models.CharField(max_length=50)
    class Meta:
        db_table="admin"
    
class doc(models.Model):
    doctor_name=models.CharField(max_length=50)
    email=models.EmailField()
    pwd=models.CharField(max_length=50)
    class Meta:
        db_table="doc"