from typing import List, Any

from Activity_Scheduler.models import *
from Activity_Scheduler.forms import *


class Counter:
    def __init__(self, noOfSections, noOfCourses):
        self.noOfSections = noOfSections
        self.counter = [[0 for j in range(noOfSections)] for i in range(noOfCourses)]

    def add(self, course, k):
        self.counter[course.count][k] = self.counter[course.count][k] + 1

    def get(self, course, k):
        return self.counter[course.count][k]


def createClassTimetable(Class: Class, Time: Timetable):
    BusyRooms = []
    FreeRooms = []
    roomL = list(Rooms.objects.all())
    if roomL:
        room = roomL[0].rooms
    else:
        flag = False
        return flag

    for i in range(Class.sections):
        if i < room:
            FreeRooms.append(i + 1)
    courses: List[Course] = list(Course.objects.filter(Class=Class))

    if courses:
        totalNoOfCourses: int = len(courses)
    else:
        flag = False
        return flag

    for i in range(1, len(courses)):

        key: Course = courses[i]

        j = i - 1
        while j >= 0 and key.crtHours > courses[j].crtHours:
            courses[j + 1] = courses[j]
            j -= 1
        courses[j + 1] = key

    for i in range(len(courses)):
        courses[i].count = i

    x = 0  # to increment or decrement courses and assign them to timetable
    tm = None
    timetable = [[[tm for col in range(5 + 5)] for col in range(Class.dwk + 5)] for row in
                 range(Class.sections + 5)]
    FreeSlots = []
    counter = Counter(Class.sections, totalNoOfCourses)
    curCourse: Course = courses[x]
    for i in range(0, 5):
        dwk = Class.dwk
        for j in range(dwk):
            classesUsed = 0
            nos = Class.sections
            for k in range(nos):
                total = 0
                while timetable[i][j][k] == tm:
                    if fit(curCourse, FreeRooms, i, j, k, timetable, counter, nos) > 3:
                        if counter.get(curCourse, k) == curCourse.crtHours:
                            break
                        leng = len(FreeRooms)
                        r = FreeRooms[leng - 1]
                        timesl = TimeSlot.objects.create(course=curCourse, teacher=curCourse.teacher, room=r, section=k,
                                                         day=i, period=j, Timetable=Time)
                        timetable[i][j][k] = timesl
                        counter.add(curCourse, k)
                        BusyRooms.append(r)
                        FreeRooms = FreeRooms[:-1]
                        classesUsed = classesUsed + 1
                    else:
                        if x < totalNoOfCourses:
                            x = 0
                            curCourse = courses[x]
                            total = total + 1
                        else:
                            x = x + 1
                            curCourse = courses[x]
                            total = total + 1
                    if total == totalNoOfCourses:
                        break
                if timetable[i][j][k] == tm:
                    s = TimeSlot(Timetable=Time)
                    s.save()
                    FreeSlots.append(s)
                    le = len(FreeSlots)
                    FreeSlots[le - 1].addFree(FreeRooms, i, j)
                if x < totalNoOfCourses - 1:
                    x = x + 1
                    curCourse = courses[x]
                else:
                    x = 0
                    curCourse = courses[x]
            while classesUsed != 0:
                leng = len(BusyRooms)
                r = BusyRooms[leng - 1]
                FreeRooms.append(r)
                BusyRooms = BusyRooms[:-1]
                classesUsed = classesUsed - 1

    nSec = Class.sections
    errorCourse, errorSec = checkForErrors(counter, courses, totalNoOfCourses, nSec)
    errorNum = len(errorCourse)
    if errorNum == 0:
        return timetable
    else:
        repairTimetable(timetable, FreeRooms, FreeSlots, counter, errorSec, nSec, errorCourse, errorNum - 1, 0)
        return timetable


def TeacherIsAvailable(timetable, i, j, teacher, sections):
    for k in range(sections):
        if timetable[i][j][k] is not None:
            if timetable[i][j][k].teacher == teacher:
                return False
    return True


def fit(course, F, i, j, k, timetable, counter, sections):
    var = 0
    if len(F) != 0:
        var = var + 2
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
                errorCourse.append(course[i])  # store course index and section index to spot the problem
                errorSec.append(j)

    return errorCourse, errorSec


def repairTimetable(timetable, FreeRooms, FreeSlots, counter, errorSec, noOfSections, errorCourse, errorNo, x):
    if len(errorCourse) - 1 == 0:
        return timetable

    curCourse = errorCourse[errorNo]
    curSection = errorSec[errorNo]

    er = errorCourse[errorNo]
    while er is not None:
        i, j = FreeSlots[x].getTime()
        if fit(curCourse, FreeRooms, i, j, curSection, timetable, counter, noOfSections) >= 3:
            if counter.get(curCourse, curSection) > curCourse.crtHours:
                break
            x = x + 1
            r = FreeSlots[x].FreeRooms[0]
            timetable[i][j][curSection](curCourse, curCourse.teacher, r)
            errorSec = errorSec[: -1]
            errorCourse = errorCourse[:-1]
        else:
            if x == len(FreeSlots) - 1:
                x = 0
                i, j = FreeSlots[x].getTime()
                x = x + 1
            else:
                i, j = FreeSlots[x].getTime()
                x = x + 1

    return timetable
