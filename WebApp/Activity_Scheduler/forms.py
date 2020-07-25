from django import forms
from Activity_Scheduler.models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


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
        fields = '__all__'


class RoomCreate(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = '__all__'


