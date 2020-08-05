"""AOA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from Activity_Scheduler.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('Register/', Register),
    path('Contact/', Contact),
    path('Login/', Register),
    path('About/', AboutUs),
    path('YourAccount/', Register),
    path('YourAccount/Help/', Help),
    path('YourAccount/mastertimetable/', Register),
    path('YourAccount/AddClass/', AddClass),
    path('YourAccount/EditInformation/', EditInfo),
    path('YourAccount/EditInformation/AddTeacher/', AddTeacher),
    path('YourAccount/EditInformation/AddRooms/', AddRooms),
    path('YourAccount/EditInformation/AddCourse/', AddCourse),
    path('YourAccount/EditInformation/ViewCourses/UpdateCourse/<int:course_id>', UpdateCourse),
    path('YourAccount/EditInformation/ViewTeacher/UpdateTeacher/<int:teacher_id>', UpdateTeacher),
    path('YourAccount/EditInformation/ViewRoom/UpdateRoom/<int:room_id>', UpdateRoom),
    path('YourAccount/EditInformation/ViewCourses/DeleteCourse/<int:course_id>', DeleteCourse),
    path('YourAccount/EditInformation/ViewTeacher/DeleteTeacher/<int:teacher_id>', DeleteTeacher),
    path('YourAccount/EditInformation/ViewCourses/', ViewCourses),
    path('YourAccount/EditInformation/ViewTeacher/', ViewTeachers),
    path('YourAccount/EditInformation/ViewRoom/', ViewRooms),
    path('YourAccount/ViewClass', ViewClass),
    path('YourAccount/YourTimetable/<int:class_id>', YourTimetable),
    path('TestTool/', TestTool),
    path('TestTool/YourTimetable', TestGeneration)
]
