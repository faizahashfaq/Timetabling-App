from django.db import models


# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=35)
    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=20)
    sections = models.SmallIntegerField()
    dwk = models.SmallIntegerField(default=7, editable=True)

    def __str__(self):
        return self.name



class Course(models.Model):
    name = models.CharField(max_length=35)
    crtHours = models.SmallIntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    Class = models.ManyToManyField(Class, default=None)

    def __str__(self):
        return self.name



class Rooms(models.Model):
    rooms: int = models.IntegerField()


class Users(models.Model):
    organization = models.CharField(max_length=130)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=30)
    email = models.EmailField(blank=True)


    @property
    def __str__(self):
        return self.username


class TimeSlot(models.Model):
    def __init__(self, course, teacher, room, FreeRooms=0, i=0, j=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.course = course
        self.teacher = teacher
        self.room = room
        self.FreeRooms = FreeRooms
        self.i = i
        self.j = j
    def addFree(self, FreeRooms, i, j):
        self.FreeRooms = FreeRooms
        self.i = i
        self.j = j
    def getTime(self):
        z = self.i
        y = self.j
        return z, y


class Timetable(models.Model):
    TimeSlot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)


class Counter:
    def __init__(self,noOfSections, noOfCourses):
        self.noOfSections = noOfSections
        self.counter = [[0 for j in range(noOfSections)] for i in range(noOfCourses)]
    def add(self, Course, k):
        self.counter[Course.id-1][k] = self.counter[Course.id-1][k] + 1
    def get(self, Course, k):
        return self.counter[Course.id-1][k]