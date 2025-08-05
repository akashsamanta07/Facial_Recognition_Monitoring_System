from django.contrib import admin
from Account.models import LoginAdmin, LoginTeacher, LoginStudent

@admin.register(LoginAdmin)
class LoginAdminAdmin(admin.ModelAdmin):
    list_display = [field.name for field in LoginAdmin._meta.fields]

@admin.register(LoginTeacher)
class LoginTeacherAdmin(admin.ModelAdmin):
    list_display = [field.name for field in LoginTeacher._meta.fields]

@admin.register(LoginStudent)
class LoginStudentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in LoginStudent._meta.fields]

