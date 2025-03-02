from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages


def home(request):
    return render(request,"index.html")

def admin_login(request):
    if request.method == 'POST':
        try:
            user_id1 = request.POST.get('username')
            password1 = request.POST.get('password')
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT user_id, user_name, password FROM account_loginadmin WHERE user_id = %s",
                    [user_id1]
                )
                row = cursor.fetchone()
                if row and row[2] == password1:
                    request.session['username']=row[1]
                    return redirect('/admin-dashboard/')
                else:
                    return render(request, "admin_login.html",{"error":"Invalid data.."}) 
        except Exception as e:
            return render(request, "admin_login.html",{"error":"Data fatch error.."})

    else:
        return render(request, "admin_login.html")



def teacher_login(request):
    if request.method == 'POST':
        try:
            user_id1 = request.POST.get('username')
            password1 = request.POST.get('password')
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT user_id, user_name, password FROM account_loginteacher WHERE user_id = %s",
                    [user_id1]
                )
                row = cursor.fetchone()
                if row and row[2] == password1:
                    request.session['username']=row[1]
                    return redirect('/teacher-dashboard/')
                else:
                    return render(request, "teacher_login.html",{"error":"Invalid data.."}) 
        except Exception as e:
            return render(request, "teacher_login.html",{"error":"Data fatch error.."})

    else:
        return render(request, "teacher_login.html")



def student_login(request):
    if request.method == 'POST':
        try:
            user_id1 = request.POST.get('username')
            password1 = request.POST.get('password')
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT user_id, user_name, password FROM account_loginstudent WHERE user_id = %s",
                    [user_id1]
                )
                row = cursor.fetchone()
                if row and row[2] == password1:
                    request.session['username']=row[1]
                    return redirect('/student-dashboard/')
                else:
                    return render(request, "student_login.html",{"error":"Invalid data.."}) 
        except Exception as e:
            return render(request, "student_login.html",{"error":"Data fatch error.."})

    else:
        return render(request, "student_login.html")


def admin_dashboard(request):
    user=request.session.get('username')
    return render(request,"admin-dashboard.html",{"username":user})


def teacher_dashboard(request):
    user=request.session.get('username')
    return render(request,"teacher-dashboard.html",{"username":user})


def student_dashboard(request):
    user=request.session.get('username')
    return render(request,"student-dashboard.html",{"username":user})


