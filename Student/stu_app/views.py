""" importing """
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError

from .models import StudentInfo


# Create your views here.

def add_student(request):
    """add student info"""
    if request.method == "POST":
        try:
            name = request.POST["name"]
            age = request.POST["age"]
            email = request.POST["email"]
            nationality = request.POST["nationality"]
            photo = request.FILES["photo"]
        except MultiValueDictKeyError:
            messages.error(request, 'fill the all fields')
            return HttpResponseRedirect('/add/')
        else:
            StudentInfo.objects.create(name=name, age=age, email=email,
                                       photo=photo, nationality=nationality)
            return HttpResponseRedirect('/')

    return render(request, 'student/add.html')


def view_student(request):
    """ show all available student """
    try:
        stu_data = StudentInfo.objects.order_by('-id')
    except StudentInfo.DoesNotExist:
        messages.error(request, 'No data available')
        return HttpResponseRedirect('/')
    else:
        return render(request, 'student/view.html', {"stu_data": stu_data})


def details_student(request, stu_id):
    """ show each student details """
    try:
        stu_info = StudentInfo.objects.get(pk=stu_id)
    except StudentInfo.DoesNotExist:
        messages.error(request, 'No data available')
        return HttpResponseRedirect('/')
    else:
        return render(request, 'student/detail.html', {"stu_info": stu_info})


def delete_student(request, stu_id):
    """ delete particular student """
    try:
        stu_data = StudentInfo.objects.get(pk=stu_id)
    except StudentInfo.DoesNotExist:
        messages.error(request, "you don't have data to delete")
        return HttpResponseRedirect('/')
    else:
        stu_data.delete()
        return HttpResponseRedirect('/')
