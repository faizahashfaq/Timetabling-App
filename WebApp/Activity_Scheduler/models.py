from django.db import models


# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=20)
    sections = models.SmallIntegerField()

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=35)
    crtHours = models.SmallIntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    Class = models.ForeignKey(Class, on_delete=models.CASCADE)

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
