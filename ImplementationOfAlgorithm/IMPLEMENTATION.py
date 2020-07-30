# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 21:46:29 2020
@author: Faiza
"""


class Course:
    def __init__(self, courseName, crtHours, teacher, ID):
        self.courseName = courseName
        self.crtHours = crtHours
        self.teacher = teacher
        self.ID = int(ID)
    def getID(self):
        return self.ID

        


class Counter:
    def __init__(self,noOfSections, noOfCourses):
        self.noOfSections = noOfSections
        self.counter = [[0 for j in range(noOfSections)] for i in range(noOfCourses)]
    def add(self, course, k):
        self.counter[course.ID-1][k] = self.counter[course.ID-1][k] + 1
    def get(self, course, k):
        return self.counter[course.ID-1][k]
    
       
    
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
    def getTime(self):
        z = self.i
        y = self.j
        return z, y
    





def GenerateDepartmentTimetable(classes, totalRooms):
    totalNoOfClasses = len(classes)
    deptTimetable = []
    FreeRooms = []
    BusyRooms = []
    x = 1
    for i in range(totalNoOfClasses):
        m = classes[i].noOfSections
        for y in range (0, m):
            if x<=totalRooms:
                FreeRooms.append(x)
                x = x + 1
        deptTimetable.append(GenerateClassTimetable(classes[i], FreeRooms, BusyRooms))
    
    return deptTimetable


def GenerateClassTimetable(Class, FreeRooms, BusyRooms):
    totalNoOfCourses = len(Class.courses)
    courses = Class.courses;
    x = 0					#to increment or decrement courses and assign them to timetable
    tm= TimeSlot(None, None, None)
    timetable = [[[tm for col in range(5+5)] for col in range(Class.dwk+5)] for row in range(Class.noOfSections+5)]
    FreeSlots = []
    counter = Counter(Class.noOfSections, totalNoOfCourses)
    curCourse = courses[x]
    for i in range(5):
        dwk = Class.dwk
        for j in range(dwk):
            classesUsed = 0
            nos = Class.noOfSections
            for k in range (nos):
                total = 0;
                while timetable[i][j][k]==tm:
                    if fit(curCourse, FreeRooms, i, j, k, timetable, counter, nos)>3:
                        if counter.get(curCourse, k) == curCourse.crtHours:
                            break
                        leng = len(FreeRooms)
                        r = FreeRooms[leng-1]
                        timetable[i][j][k]= TimeSlot(curCourse, curCourse.teacher, r)
                        counter.add(curCourse, k)
                        BusyRooms.append(r)
                        FreeRooms = FreeRooms[:-1]
                        classesUsed=classesUsed+1
                    else:
                        if x<totalNoOfCourses:
                            x=0
                            curCourse = courses[x]
                            total = total + 1
                        else:
                            x = x+1
                            curCourse = courses[x]
                            total = total + 1
                    if total == totalNoOfCourses:
                        break;
                if timetable[i][j][k]==tm:
                    FreeSlots.append(tm)
                    le = len(FreeSlots)
                    FreeSlots[le-1].addFree(FreeRooms, i, j)
                if x<totalNoOfCourses-1:
                    x = x+1
                    curCourse = courses[x]  
                else:
                    x=0
                    curCourse = courses[x]
            while classesUsed!=0:
                leng = len(BusyRooms)
                r = BusyRooms[leng-1]
                FreeRooms.append(r)
                BusyRooms = BusyRooms[:-1]
                classesUsed=classesUsed-1
                
    nSec = Class.noOfSections
    errorCourse, errorSec = checkForErrors(counter, courses, totalNoOfCourses, nSec)
    errorNum = len(errorCourse)
    if errorNum == 0:
        return timetable
    else:
        #repairTimetable(timetable, FreeRooms, FreeSlots, counter, errorSec, nSec, errorCourse, errorNum-1, 0)
        return timetable
    
   
    
    
def TeacherIsAvailable(timetable, i, j, teacher, sections):
    for k in range (sections):
        if (timetable[i][j][k]!=None):
            if (timetable[i][j][k].teacher == teacher):
                return False
    return True    
        
        

    
    
def fit(course, F,i, j, k, timetable, counter, sections):
	var=0
	if len(F)!=0:
		var = var+2
	if TeacherIsAvailable(timetable, i, j, course.teacher, sections):
		var = var + 1
	if course.crtHours > counter.get(course, k):
		var = var + 1
	return var

    
def checkForErrors(counter, course, totalCourses, noOfSections):

    errorCourse = []
    errorSec = []
    for i in range(totalCourses):
        for j in range(noOfSections):
            if counter.get(course[i], j) != course[i].crtHours:
                errorCourse.append(course[i])			 #store course index and section index to spot the problem
                errorSec.append(j)
				
    return errorCourse, errorSec


def repairTimetable (timetable, FreeRooms, FreeSlots, counter, errorSec, noOfSections, errorCourse, errorNo, x):
    if (len(errorCourse)-1 == 0):
        return timetable
	
    curCourse = errorCourse[errorNo]
    curSection = errorSec[errorNo]
    
    er = errorCourse[errorNo]
    while er!=None:
        i, j = FreeSlots[x].getTime()
        if fit(curCourse, FreeRooms, i, j, curSection, timetable, counter, noOfSections) >= 3 :
            if counter.get(curCourse, curSection)>curCourse.crtHours:
                break
            x = x+1
            r = FreeSlots[x].FreeRooms[0]
            timetable[i][j][curSection](curCourse, curCourse.teacher, r)
            errorSec = errorSec[: -1]
            errorCourse = errorCourse[:-1]
        else:
            if x == len(FreeSlots)-1:
                x=0
                i, j = FreeSlots[x].getTime()
                x=x+1
            else:
                i, j = FreeSlots[x].getTime()
                x = x+1

    repairTimetable(timetable, FreeRooms, FreeSlots, counter, errorSec, errorCourse, errorNo-1, x)


    
    
def printCourses(timetable, dwk, i, k):
    for x in range(dwk):
        if(timetable[i][x][k].course==None):
            print('Free slot', end='\t')
        else:
            print('\t', timetable[i][x][k].course.courseName,' | ', end='\t')
        
def printTeachers(timetable, dwk, i, k):
    for x in range(dwk):
        if(timetable[i][x][k].course==None):
            print('\t\t', end='\t')
        else:
            print(timetable[i][x][k].teacher,' | ', end='\t')
        
def printRooms(timetable, dwk, i, k):
    for x in range(dwk):
        if(timetable[i][x][k].course==None):
            print('\t\t', end='\t')
        else:
            print('Room # ',timetable[i][x][k].room, ' | ', end='\t')



DBMS = Course("DBMS", 3, "Atif", 1)
AOA = Course("AOA", 3, "Samyan", 2)
OS = Course("OS", 3, "Amna", 3)
MVC = Course("MVC", 2, "Rubina", 4)
TAF = Course("TAF", 3, "Tauqir", 5)
DSA = Course("DSA", 3, "hina", 6)

courses = [DBMS, AOA, OS, MVC, TAF, DSA]

for i in range(1, len(courses)): 
  
        key = courses[i] 
        
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key.crtHours > courses[j].crtHours : 
                courses[j+1] = courses[j] 
                j -= 1
        courses[j+1] = key 

for i in range(len(courses)):
    courses[i].ID = i+1

noOfSections = 3
dwk = 7
totalRooms = 3
ses2018 = Class(courses, noOfSections, dwk)

classes = [ses2018]

timetable = [[ [None for col in range(5)] for col in range(dwk)] for row in range(noOfSections)]
deptTimetable = [timetable]

deptTimetable = GenerateDepartmentTimetable(classes, totalRooms)

timetable = deptTimetable[0]

print('  ', '  ', 'Period 1\t', 'Period 2\t', 'Period 3\t', 'Period 4\t', 'Period 5\t', 'Period 6\t', 'Period 7\t')
for i in range(5):
    print('\nSection A: ', printCourses(timetable, dwk, i, 0))
    print('\t\t', printTeachers(timetable, dwk, i, 0))
    print('\t\t', printRooms(timetable, dwk, i, 0))
    print('\nSection B: ', printCourses(timetable, dwk, i, 1))
    print('\t\t', printTeachers(timetable, dwk, i, 1))
    print('\t\t', printRooms(timetable, dwk, i, 1))
    print('\nSection C: ', printCourses(timetable, dwk, i, 2))
    print('\t\t', printTeachers(timetable, dwk, i, 2))
    print('\t\t', printRooms(timetable, dwk, i, 2))