from django.shortcuts import render,redirect,get_object_or_404
from .models import Student
from django.contrib import messages



def home(request,st_id=None):
    if st_id:
        student = get_object_or_404(Student,id=st_id)
    else:
        student = None

    if request.method=='POST':
        name = request.POST['name'].title()
        email = request.POST['email']
        contact = request.POST['contact']
        address = request.POST['address'].title()

        if student:
            student.name = name
            student.email = email
            student.contact = contact
            student.address = address
            student.save()
            messages.success(request,"Record Updated Successfully")
            return redirect('home')
        else:
            if Student.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists...')
            elif Student.objects.filter(contact=contact).exists():
                messages.error(request, 'Contact already exists...')
            else:
                student = Student.objects.create(name=name,
                                                 email=email,
                                                 contact=contact,
                                                 address=address)
                student.save()
                messages.success(request,"Record Added Successfully")
                return redirect('home')
    else:
        students = Student.objects.all()
        return render (request,'index.html',{'students':students,'student':student})

def delete(request,st_id):
    student = Student.objects.filter(id=st_id)
    student.delete()
    messages.success(request,"Record Deleted Successfully")
    return redirect('home')



