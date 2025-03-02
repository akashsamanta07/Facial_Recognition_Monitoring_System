"""
URL configuration for Facial_Recognition_Monitoring_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="index"),
    path('student-login/',views.student_login,name="student_login"),
    path('teacher-login/',views.teacher_login,name="teacher_login"),
    path('admin-login/',views.admin_login,name="admin_login"),
    path('admin-dashboard/',views.admin_dashboard,name="admin_dashboard"),
    path('teacher-dashboard/',views.teacher_dashboard,name="teacher_dashboard"),
    path('student-dashboard/',views.student_dashboard,name="student_dashboard"),
    path('teacher-logout/',views.teacher_logout,name="teacher_logout"),
    path('student-logout/',views.student_logout,name="student_logout"),
    path('admin-logout/',views.admin_logout,name="admin_logout"),
    
]
