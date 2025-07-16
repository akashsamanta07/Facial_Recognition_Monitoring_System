from django.db import models

# Create your models here.

class LoginAdmin(models.Model):
    user_id=models.CharField(max_length=20,primary_key=True)
    user_name=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    email = models.EmailField(default='default@example.com') 
    department=models.CharField(max_length=20,default='')
    year = models.CharField(max_length=4,default="2024")
    
    
    
class LoginTeacher(models.Model):
    user_id=models.CharField(max_length=20,primary_key=True)
    user_name=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    email = models.EmailField(default='default@example.com') 
    department=models.CharField(max_length=20,default='')
    year = models.CharField(max_length=4,default="2024")

    

class LoginStudent(models.Model):
    user_id=models.CharField(max_length=20,primary_key=True)
    user_name=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    email = models.EmailField(default='default@example.com') 
    department=models.CharField(max_length=20,default='')
    year = models.CharField(max_length=4,default="2024")

