# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 18:39:01 2020

@author: Faiza
"""


import IMPLEMENTATION as imp




DBMS = imp.Course("Database Systems", 3, "Atif")
AOA = imp.Course("Analysis of Algorithm", 3, "Samyan")
OS = imp.Course("Operating systems", 3, "Amna")
MVC = imp.Course("Multivariate Calculus", 2, "Rubina")
TAF = imp.Course("Theory of Automata and Formal Languages", 3, "Tauqir")
courses = [DBMS, AOA, OS, MVC, TAF]
noOfSections = 3
dwk = 7
totalRooms = 3
ses2018 = imp.Class(courses, noOfSections, dwk)

classes = [ses2018]

timetable = [[ [0 for col in range(5)] for col in range(dwk)] for row in range(noOfSections)]
deptTimetable = [timetable]

deptTimetable = imp.GenerateDepartmentTimetable(classes, totalRooms)

print(deptTimetable[0])