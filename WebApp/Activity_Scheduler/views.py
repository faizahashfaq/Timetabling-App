from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from Activity_Scheduler.models import *
from Activity_Scheduler.forms import *
from templates import *

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


def TestGeneration(request):

    return render(request, 'TestGeneration.html')