from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.contrib.auth import authenticate
# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from Activity_Scheduler.models import *
from Activity_Scheduler.forms import *
from templates import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def homepage(request):
    html = '''<h1>Activity Scheduler</h1>Hello'''
    return HttpResponse(html)


def Register(request):
    html = '''<h1>Register with us</h1>Hello'''
    return HttpResponse(html)


def Contact(request):
    html = '''<h1>Contact us</h1>Hello'''
    return HttpResponse(html)


def AboutUs(request):
    html = '''<h1>About us<h1>Hello'''
    return HttpResponse(html)


def TestTool(request):
    return render(request, 'TestToolPage.html')


def YourPage(request):
    html = '''<h1>Logged in<h1>Hello'''
    return HttpResponse(html)


def TestGeneration(request):
    return render(request, 'TestGeneration.html')


def EditInfo(request):
    return render(request, 'YourAccount/EditInformation.html')


#@login_required
def AddTeacher(request):
    form = TeacherCreate()
    if request.method == 'POST':
        form = TeacherCreate(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request, f'New teacher has been added!')
            return redirect('/YourAccount/EditInformation')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "EditInfo">reload</a>""")
    return render(request, 'YourAccount/EditInformationAddAcc.html', {'form': form})


#def AddClass(request):
 #   if request.method == 'POST':
  #      form = ClassCreate()
   #     if request.method == 'POST':
    #        form = ClassCreate(request.POST)
     #       if form.is_valid():
      #          form.save()
       #         name = form.cleaned_data.get('name')
        #        messages.success(request, f'New class has been added!')
         ##  else:
           #     return HttpResponse("""your form is wrong, reload on <a href = "EditInfo">reload</a>""")
 #   return render(request, 'YourAccount/EditInformationAddAcc.html', {'form': form})


def AddCourse(request):
    form = CourseCreate()
    if request.method == 'POST':
        form = CourseCreate(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request, f'New course has been added!')
            return redirect('')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "EditInfo">reload</a>""")
    return render(request, 'YourAccount/EditInformationAddCourse.html', {'form': form})


def AddRooms(request):
    form = RoomCreate()
    if request.method == 'POST':
        form = RoomCreate(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request, f'Rooms have been updated!')
            return redirect('')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "EditInfo">reload</a>""")
    return render(request, 'YourAccount/EditInformationAddRooms.html', {'form': form})