from django.contrib import admin
from Account.models import LoginAdmin, LoginTeacher, LoginStudent

class Admin(admin.ModelAdmin):
    list_display = ("user_id","user_name", "password")
admin.site.register(LoginAdmin, Admin)

class Teacher(admin.ModelAdmin):
    list_display = ("user_id","user_name", "password")
admin.site.register(LoginTeacher, Teacher)

class Student(admin.ModelAdmin):
    list_display = ("user_id", "user_name","password")
admin.site.register(LoginStudent, Student)

