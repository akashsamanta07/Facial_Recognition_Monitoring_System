from django.db import models

# Create your models here.

class LoginAdmin(models.Model):
    user_id=models.CharField(max_length=20,primary_key=True)
    user_name=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    
    
    
class LoginTeacher(models.Model):
    user_id=models.CharField(max_length=20,primary_key=True)
    user_name=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    

class LoginStudent(models.Model):
    user_id=models.CharField(max_length=20,primary_key=True)
    user_name=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
