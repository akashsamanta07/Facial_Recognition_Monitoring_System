from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages
import openpyxl
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from django.views.decorators.cache import never_cache

def home(request):
    return render(request,"index.html")

@never_cache
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
                    request.session['user_id']=row[0]
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

@never_cache
def admin_dashboard(request):
    if 'user_id' not in request.session:
        return redirect("index")
    username=request.session.get('username')
    message=datetime.now()
    if request.method == 'POST':
        table_name="table_"+str(request.session.get('user_id'))
        try:
            with connection.cursor() as cursor:
                cursor.execute(f'''
                    CREATE TABLE IF NOT EXISTS `{table_name}` (
                        id VARCHAR(20) PRIMARY KEY, 
                        name VARCHAR(25),
                        subject VARCHAR(25),
                        semester VARCHAR(25),
                        year VARCHAR(4),
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                ''')
            excel_file = request.FILES.get('excelFile')
            if excel_file:
                wb = openpyxl.load_workbook(excel_file)
                sheet = wb.active
                with connection.cursor() as cursor:
                    for row in sheet.iter_rows(min_row=2, values_only=True): 
                        student_id, name, subject, semester, year = row
                        if not student_id: 
                            continue
                        cursor.execute(
                            f'''INSERT INTO `{table_name}` (id, name, subject, semester, year)
                                VALUES (%s, %s, %s, %s, %s);''',
                            [str(student_id), str(name), str(subject), str(semester), str(year)]
                        )
                message = "Excel data uploaded successfully."
            else:
                student_id = request.POST.get('userId')
                name = request.POST.get('name')
                subject = request.POST.get('subject')
                semester = request.POST.get('semester')
                year = request.POST.get('year')
                if student_id and name and subject and semester and year:
                    with connection.cursor() as cursor:
                        cursor.execute(
                            f'''INSERT INTO `{table_name}` (id, name, subject, semester, year)
                                VALUES (%s, %s, %s, %s, %s);''',
                            [student_id, name, subject, semester, year]
                        )
                    message = "Manual data added successfully."
                else:
                     message="Invalid data"
        except Exception as e:
            message = "Error occurred."
    return render(request,"admin-dashboard.html",{"username":username,"message":message})


def teacher_dashboard(request):
    user=request.session.get('username')
    return render(request,"teacher-dashboard.html",{"username":user})


def student_dashboard(request):
    user=request.session.get('username')
    return render(request,"student-dashboard.html",{"username":user})

def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('index')


