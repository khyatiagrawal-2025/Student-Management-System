from django.shortcuts import render, redirect

from .models import Student

# Create your views here.

def student_home(request):

    students_data = Student.objects.all()

    print(students_data)

    data = {
        "students_data": students_data
    }

    return render(request,"student/student_home.html",data)

def add_student(request):

    if request.method == "POST":
        student_name = request.POST.get("input_name")
        student_email = request.POST.get("input_email")
        student_phone_number = request.POST.get("input_phone_number")
        student_course = request.POST.get("input_course")

        Student.objects.create(
            name = student_name,
            email = student_email,
            phone_number = student_phone_number,
            course = student_course
        )

        return redirect("student_home")
    
    return render(request,"student/add_student.html")

def delete_student(request, id):
    my_student = Student.objects.get(id = id)
    my_student.delete()
    return redirect("student_home")

def update_student(request, id):
    student = Student.objects.get(id = id)

    if request.method == "POST":
        student.name = request.POST.get("name")
        student.email = request.POST.get("email")
        student.phone_number = request.POST.get("phone")
        student.course = request.POST.get("course")

        student.save()

        return redirect("student_home")

    parameters = {
        "student": student
    }

    return render(request, "student/update_student.html")