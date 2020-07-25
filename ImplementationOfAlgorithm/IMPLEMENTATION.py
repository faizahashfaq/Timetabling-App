# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 21:46:29 2020

@author: Faiza
"""
from collections import deque

class Course:
    def __init__(self, courseName, crtHours, teacher, ID):
        self.courseName = courseName
        self.crtHours = crtHours
        self.teacher = teacher
        self.ID = ID
    def getID(self):
        return self.ID

        


class Counter:
    def __init__(self,noOfSections, noOfCourses):
        self.noOfSections = noOfSections
        self.counter = [[0 for j in range(noOfCourses)] for i in range(noOfSections)]
    def add(self, k,course):
        self.counter[course.id][k] = self.counter[course.id][k] + 1
    def get(self, k, course):
        IDA = course.getID()
        return self.counter[IDA][k]
    
       
    
class Class:
      def __init__(self,courses,noOfSections, dwk):
          self.courses = courses
          self.noOfSections = noOfSections
          self.dwk = dwk


class TimeSlot:
    def __init__(self, course,teacher,room,FreeRooms = 0, i=0,j=0):
        self.course = course
        self.teacher = teacher
        self.room = room
        self.FreeRooms = FreeRooms
        self.i = i
        self.j=j
    def addFree(self, FreeRooms, i, j):
        self.FreeRooms = FreeRooms
        self.i = i
        self.j = j
    def getTime(self, x):
        z = self.i
        y = self.j
        return z, y
    





def GenerateDepartmentTimetable(classes, totalRooms):
    totalNoOfClasses = len(classes)
    deptTimetable = []
    FreeRooms = deque()
    BusyRooms = deque()
    x = 1
    for i in range(totalNoOfClasses):
        m = classes[i].noOfSections
        for x in range (m):
            if x>=totalRooms:
                FreeRooms.append(x)
        deptTimetable[i] = GenerateClassTimetable(classes[i], FreeRooms, BusyRooms)
    
    return deptTimetable


def GenerateClassTimetable(Class, FreeRooms, BusyRooms):
    totalNoOfCourses = len(Class.courses)
    courses = Class.courses;
    x = 0					#to increment or decrement courses and assign them to timetable
    fm = None
    timetable = [[ [fm for col in range(5)] for col in range(Class.dwk)] for row in range(Class.noOfSections)]
    FreeSlots = []
    y = 0
    
    counter = Counter(Class.noOfSections, totalNoOfCourses)
    curCourse = Class.courses[x]
    for i in range(5):
        dwk = Class.dwk
        for j in range(dwk):
            classesUsed = 0
            nos = Class.noOfSections
            for k in range (nos):
                while timetable[i][j][k]==None:
                    if fit(curCourse, FreeRooms, i, j, k, timetable, counter, nos)>3:
                        r = FreeRooms.pop()
                        timetable[i][j][k](curCourse, curCourse.teacher, r)
                        BusyRooms.append(r)
                        classesUsed=classesUsed+1
                    else:
                        if x>totalNoOfCourses:
                            x=0
                            curCourse = courses[x]
                        else:
                            x = x+1
                            curCourse = courses[x]
                if timetable[i][j][k]==0:
                    FreeSlots[y].addFree(FreeRooms, i, j)
                    y = y + 1
                if x>totalNoOfCourses:
                    x=0
                    curCourse = courses[x]
                else:
                    x = x+1
                    curCourse = courses[x]
            while classesUsed!=0:
                r = BusyRooms.pop()
                FreeRooms.append(r)
                classesUsed=classesUsed-1
                
    nSec = Class.noOfSections
    errorCourse, errorSec = checkForErrors(counter, courses, totalNoOfCourses, nSec)
    errorNum = len(errorCourse)
    if errorNum == 0:
        return timetable
    else:
        repairTimetable(timetable, FreeRooms, FreeSlots, counter, errorSec, nSec, errorCourse, errorNum, 0)
        return timetable
    
   
    
    
def TeacherIsAvailable(timetable, i, j, teacher, sections):
    for k in range (sections):
        if (timetable[i][j][k]!=None):
            if (timetable[i][j][k].teacher == teacher):
                return False
    return True    
        
        

    
    
def fit(course, F,i, j, k, timetable, counter, sections):
	var=0
	if F:
		var = var+1
	if TeacherIsAvailable(timetable, i, j, course.teacher, sections):
		var = var + 1
	if course.crtHours > counter.get(course, k):
		var = var + 1
	if timetable[i][j-2][k] != course:
		var = var+1
	return var

    
def checkForErrors(counter, course, totalCourses, noOfSections):
    x = 0
	
    errorCourse = []
    errorSec = []
    for i in range(totalCourses):
        for j in range(noOfSections):
            if counter.counter[i][j] != course[i].crtHours:
                errorCourse[x] = course[i]			 #store course index and section index to spot the problem
                errorSec[x] = j
                x = x+1
				
    return errorCourse and errorSec


def repairTimetable (timetable, FreeRooms, FreeSlots, counter, errorSec, noOfSections, errorCourse, errorNo, x):
    if (len(errorCourse) == 0):
        return timetable
	
    curCourse = errorCourse[errorNo]
    curSection = errorSec[errorNo]
    
    er = errorCourse[errorNo]
    while er!=None:
        i, j = FreeSlots[x].getTime()
        if fit(curCourse, FreeRooms, i, j, curSection, timetable, counter, noOfSections) > 3 :
            x = x+1
            r = FreeRooms.pop()
            timetable[i][j][curSection](curCourse, curCourse.teacher, r)
            FreeRooms.append(r)
            errorSec[errorNo] = None
            errorCourse[errorNo] = None
        else:
            if x == len(FreeSlots):
                x=0
                i, j = FreeSlots[x].getTime()
                x=x+1
            else:
                i, j = FreeSlots[x].getTime()
                x = x+1

    repairTimetable(timetable, FreeRooms, FreeSlots, counter, errorSec, errorCourse, errorNo-1, x)




DBMS = Course("Database Systems", 3, "Atif", 1)
AOA = Course("Analysis of Algorithm", 3, "Samyan", 2)
OS = Course("Operating systems", 3, "Amna", 3)
MVC = Course("Multivariate Calculus", 2, "Rubina", 4)
TAF = Course("Theory of Automata and Formal Languages", 3, "Tauqir", 5)
courses = [DBMS, AOA, OS, MVC, TAF]
noOfSections = 3
dwk = 7
totalRooms = 3
ses2018 = Class(courses, noOfSections, dwk)

classes = [ses2018]

timetable = [[ [None for col in range(5)] for col in range(dwk)] for row in range(noOfSections)]
deptTimetable = [timetable]

deptTimetable = GenerateDepartmentTimetable(classes, totalRooms)

print(deptTimetable[0])