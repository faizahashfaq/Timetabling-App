from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.contrib.auth import authenticate
# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.core.exceptions import MultipleObjectsReturned
from Activity_Scheduler.models import *
from Activity_Scheduler.forms import *
from templates import *
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from Activity_Scheduler.Functions import *


def homepage(request):
    return render(request, 'homepage.html')


def Register(request):
    return render(request, 'inProgress.html')


def Contact(request):
    return render(request, 'Contact.html')


def AboutUs(request):
    return render(request, 'About.html')


def TestTool(request):
    return render(request, 'TestToolPage.html')


def YourPage(request):
    html = '''<h1>Logged in<h1>Hello'''
    return HttpResponse(html)


def TestGeneration(request):
    return render(request, 'TestGeneration.html')


def EditInfo(request):
    return render(request, 'YourAccount/EditInformation.html')


def Help(request):
    return render(request, 'YourAccount/Help.html')

# @login_required
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


def AddClass(request):
    form = ClassCreate()
    if request.method == 'POST':
        form = ClassCreate(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request, f'New class has been added!')
            return redirect('/YourAccount/EditInformation')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "EditInfo">reload</a>""")
    return render(request, 'Activity_Scheduler/YourAccount.html', {'form': form})


def AddCourse(request):
    form = CourseCreate()
    if request.method == 'POST':
        form = CourseCreate(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request, f'New course has been added!')
            return redirect('/YourAccount/EditInformation')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "EditInfo">reload</a>""")
    return render(request, 'YourAccount/EditInformationAddCourse.html', {'form': form})


def AddRooms(request):
    form = RoomCreate()
    room = list(Rooms.objects.all())
    if room:
        messages.success(request, f'Room numbers have already been added for your account, you can only update them now!')
        return redirect('/YourAccount/EditInformation')
    if request.method == 'POST':
        form = RoomCreate(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request, f'Rooms have been added!')
            return redirect('/YourAccount/EditInformation')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "EditInfo">reload</a>""")
    return render(request, 'YourAccount/EditInformationAddRooms.html', {'form': form})


def UpdateCourse(request, course_id):
    course_id = int(course_id)
    try:
        course_sel = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return redirect('/YourAccount/EditInformation')
    course_form = CourseCreate(request.POST or None, instance=course_sel)
    if course_form.is_valid():
        course_form.save()
        messages.success(request, f'Course has been updated!')
        return redirect('/YourAccount/EditInformation')
    return render(request, 'YourAccount/update/updateCourse.html', {'form': course_form})


def UpdateTeacher(request, teacher_id):
    teacher_id = int(teacher_id)
    try:
        teacher_sel = Teacher.objects.get(id=teacher_id)
    except Teacher.DoesNotExist:
        return redirect('/YourAccount/EditInformation')
    teacher_form = TeacherCreate(request.POST or None, instance=teacher_sel)
    if teacher_form.is_valid():
        teacher_form.save()
        messages.success(request, f'Teacher has been updated!')
        return redirect('/YourAccount/EditInformation')
    return render(request, 'YourAccount/update/updateteacher.html', {'form': teacher_form})


def UpdateRoom(request, room_id):
    room_id = int(room_id)
    try:
        room_sel = Rooms.objects.get(id=room_id)
    except Rooms.DoesNotExist:
        return redirect('/YourAccount/EditInformation')
    room_form = RoomCreate(request.POST or None, instance=room_sel)
    if room_form.is_valid():
        room_form.save()
        messages.success(request, f'Rooms have been updated!')
        return redirect('/YourAccount/EditInformation')
    return render(request, 'YourAccount/update/updateroom.html', {'form': room_form})


def ViewCourses(request):
    view = Course.objects.all()
    return render(request, 'YourAccount/viewCourse.html', dict(view=view))


def ViewTeachers(request):
    view = Teacher.objects.all()
    return render(request, 'YourAccount/viewTeacher.html', dict(view=view))


def ViewRooms(request):
    view = Rooms.objects.all()
    return render(request, 'YourAccount/viewRoom.html', dict(view=view))


def DeleteCourse(request, course_id):
    course_id = int(course_id)
    try:
        course_sel = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return redirect('/YourAccount/EditInformation')
    course_sel.delete()
    messages.success(request, f'Course has been deleted!')
    return redirect('/YourAccount/EditInformation')


def DeleteTeacher(request, teacher_id):
    teacher_id = int(teacher_id)
    try:
        teacher_sel = Teacher.objects.get(id=teacher_id)
    except Course.DoesNotExist:
        return redirect('/YourAccount/EditInformation')
    teacher_sel.delete()
    messages.success(request, f'Teacher has been deleted!')
    return redirect('/YourAccount/EditInformation')


def ViewClass(request):
    view = Class.objects.all()
    return render(request, 'YourAccount/viewClass.html', dict(view=view))


def YourTimetable(request, class_id):
    class_id = int(class_id)
    try:
        class_s = Class.objects.get(id=class_id)
    except Class.DoesNotExist:
        return redirect('/YourAccount')
    day = 5
    noOfSec = class_s.sections
    dwk = class_s.dwk
    Flag = True
    message = 'None'
    try:
        timetable = Timetable.objects.get(Class=class_s)
    except Timetable.DoesNotExist:
        timetable = Timetable.objects.create(Class=class_s)


    try:
        t = TimeSlot.objects.get(Timetable=timetable)
    except MultipleObjectsReturned:
        TimeSlot.objects.all().delete()

        Flag = createClassTimetable(class_s, timetable)

        if not Flag:
            messages.success(request, "Incomplete fields!")
            return redirect('/YourAccount/EditInformation')
        trying = TimeSlot.objects.filter(Timetable=timetable)
        return render(request, 'YourAccount/YourTable.html',
                      {'timetable': timetable, 'trying': trying, 'day': day, 'noOfSec': noOfSec, 'dwk': dwk})
    except TimeSlot.DoesNotExist:
        Flag = createClassTimetable(class_s, timetable)

        if not Flag:
            messages.success(request, "Incomplete fields!")
            return redirect('/YourAccount/EditInformation')

        trying = TimeSlot.objects.filter(Timetable=timetable)
        return render(request, 'YourAccount/YourTable.html',
                      {'timetable': timetable, 'trying': trying, 'day': day, 'noOfSec': noOfSec, 'dwk': dwk})

