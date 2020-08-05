from django import forms
from Activity_Scheduler.models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field


class TeacherCreate(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class ClassCreate(forms.ModelForm):
    class Meta:
        model = Class
        fields = '__all__'


class CourseCreate(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'crtHours', 'teacher', 'Class']

    helper = FormHelper()
    helper.layout = Layout(Field('Count', type="hidden"))


class RoomCreate(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = '__all__'


class TimetableCreate(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = '__all__'


class TimeSlotCreate(forms.ModelForm):
    class Meta:
        model = TimeSlot
        fields = '__all__'
