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
    path('teacher-forget/',views.teacher_forget,name="teacher_forget"),
    path('admin-forget/',views.admin_forget,name="admin_forget"),
    path('student-forget/',views.student_forget,name="student_forget"),
    path('logout/',views.logout,name="logout"),
    path('update-teacher/',views.update_teacher,name="update_teacher"),
    path('update-student/',views.update_student,name="update_student"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)