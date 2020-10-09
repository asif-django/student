from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Student_info


# Create your views here.

def StudentAdd(request):
    if request.method == "POST":
        name = request.POST["name"]
        age = request.POST["age"]
        email = request.POST["email"]
        nationality = request.POST["nationality"]
        photo = request.FILES["Photo"]
        print(photo)

        s = Student_info.objects.create(name=name, age=age, email=email,
                                        photo=photo, nationality=nationality)
        s.save()

    return render(request, 'student/add.html')


def StudentView(request):
    stu_data = Student_info.objects.all()
    return render(request, 'student/view.html', {"stu_data": stu_data})


def StudentDetails(request, stu_id):
    stu_info = Student_info.objects.filter(pk=stu_id)
    return render(request, 'student/detail.html', {"stu_info": stu_info})

def StudentDelete(request, stu_id):
    stu_data = Student_info.objects.get(pk=stu_id)
    stu_data.delete()
    return HttpResponseRedirect('/view/')