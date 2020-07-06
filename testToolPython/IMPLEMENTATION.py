# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 21:46:29 2020

@author: Faiza
"""


class Course:
    def _init_(self, courseName, crtHours, teacher):
        self.courseName = courseName
        self.crtHours = crtHours
        self.teacher = teacher


  
class Teacher:
    def _init_(self, teacherName, course = []):
        self.teacherName = teacherName
        self.course = course.append(course)
        


class Counter:
    def _init_(self,noOfSections, noOfCourses):
        self.noOfSections = noOfSections
        self.counter[noOfCourses][noOfSections]
    def add(self, k,course):
        self.counter[course][k] = self.counter[course][k] + 1
    def get(self, k,course):
        return self.counter[course][k]
    
       
    
class Class:
      def _init_(self,courses,noOfSections, dwk):
          self.courses = courses
          self.noOfSections = noOfSections
          self.dwk = dwk


class TimeSlot:
    def _init_(self, course,teacher,room,FreeRooms = 0, i=0,j=0):
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
    





def GenerateDepartmentTimetable(classes, Rooms):
    totalNoOfClasses = len(classes)
    deptTimetable = []
    FreeRooms = []
    BusyRooms = []
    x = 0
    for i in range(0, totalNoOfClasses):
        m = classes[i].noOfSections
        for x in range (m):
            FreeRooms.push(x)
        deptTimetable[i] = GenerateClassTimetable(classes[i], FreeRooms, BusyRooms)
    
    return deptTimetable


def GenerateClassTimetable(Class, FreeRooms, BusyRooms):
    totalNoOfCourses = len(Class.courses)
    x = 0					#to increment or decrement courses and assign them to timetable
    timetable = [[ [0 for col in range(5)] for col in range(Class.dwk)] for row in range(Class.noOfSections)]
    FreeSlots = []
    y = 0
    counter = [Class.noOfSections, totalNoOfCourses]
    counter = [[[] for j in range(Class.noOfSections)] for i in range(totalNoOfCourses)]
    curCourse = Class.courses[x]
    for i in range(5):
        dwk = Class.dwk
        for j in range(dwk):
            classesUsed = 0
            nos = Class.noOfSections
            for k in range (nos):
                while timetable[i][j][k]==0:
                    if fit(curCourse, FreeRooms, i, j, k, timetable, counter)>3:
                        r = FreeRooms.pop()
                        timetable[i][j][k](curCourse, curCourse.teacher, r)
                        BusyRooms.push(r)
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
                r = B.pop()
                F.push(r)
                classesUsed=classesUsed-1
                
    errorCourse, errorSec = checkForErrors(counter, courses, totalNoOfCourses, noOfSections)
    errorNum = len(errorCourse)
    if errorNum == 0:
        return timetable
    else:
        repairTimetable(timetable, FreeRooms, FreeSlots, counter, errorSec, errorCourse, errorNum, 0)
        return timetable
    
    
    
def fit(course, F,i, j, k, timetable, counter):
	var=0
	if F.top!= False:
		var = var+1
	if TeacherIsAvailable(timetable, i, j, course.teacher):
		var = var + 1
	if course.crtHours > counter.get(course, k):
		var = var + 1
	if timetable[i][j-2][k] != course:
		var = var+1
	return var

    
def checkForErrors(counter, course, totalCourses, noOfSections):
	x = 0
	for i in range(totalCourses):
		for j in range(noOfSections):
			if counter.counter[i][j] != course[i].crtHours:
				errorCourse[x] = course[i]			 #store course index and section index to spot the problem
				errorSec[x] = j
				x = x+1
				
	return errorCourse and errorSec


def repairTimetable (timetable, FreeRooms, FreeSlots, counter, errorSec, errorCourse, errorNo, x):
	if (len(errorCourse) == 0):
		return timetable
	
	else:
		curCourse = errorCourse[errorNo]
		curSection = errorSec[errorNo]
		while (errorCourse[errorNo]!= NONE):
			if fit(curCourse, FreeRooms, i, j, curSection, timetable, counter) > 3 :
				i, j = FreeSlots[x].getTime()
				x = x+1
				r = FreeRooms.pop()
				timetable[i][j][curSection](curCourse, curCourse.teacher, r)
				FreeRooms.push(r)
				errorSec[errorNo] = NONE
				errorCourse[errorNo] = NONE
			else:
				if x == lengthOf(FreeSlots):
					x=0
					i, j = FreeSlots[x].getTime()
					x=x+1
				else:
					i, j = FreeSlots[x].getTime()
					x = x+1

		repairTimetable(timetable, FreeRooms, FreeSlots, counter, errorSec, errorCourse, errorNo-1, x)
