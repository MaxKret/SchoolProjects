# File: Project1.py
# Student: Maxwell Kretschmer
# UT EID: mtk739
# Course Name: CS303E
# 
# Date Created: 3/22/21
# Date Last Modified: 3/23/21
# Description of Program: Takes in student name, 3 hw grades, 2 exam grades, and 2 project grades, finds their averages, and then calculates the weighted average and lettergrade.

name = input("Enter the student's name: ")
print("")
#HW
print("HOMEWORKS:")
while(True):
    hw1Grade = float(input("  Enter HW1 grade: "))
    if(hw1Grade>=0 and hw1Grade<=10):
        break
    else:
        print("  Grade must be in range [0..10]. Try again.")
while(True):
    hw2Grade = float(input("  Enter HW2 grade: "))
    if(hw2Grade>=0 and hw2Grade<=10):
        break
    else:
        print("  Grade must be in range [0..10]. Try again.")
while(True):
    hw3Grade = float(input("  Enter HW3 grade: "))
    if(hw3Grade>=0 and hw3Grade<=10):
        break
    else:
        print("  Grade must be in range [0..10]. Try again.")
print("")

#PROJ
print("PROJECTS:")
while(True):
    pj1Grade = float(input("  Enter Project1 grade: "))
    if(pj1Grade>=0 and pj1Grade<=100):
        break
    else:
        print("  Grade must be in range [0..100]. Try again.")
while(True):
    pj2Grade = float(input("  Enter Project2 grade: "))
    if(pj2Grade>=0 and pj2Grade<=100):
        break
    else:
        print("  Grade must be in range [0..100]. Try again.")
print("")

#EXAM
print("EXAMS:")
while(True):
    ex1Grade = float(input("  Enter Exam1 grade: "))
    if(ex1Grade>=0 and ex1Grade<=100):
        break
    else:
        print("  Grade must be in range [0..100]. Try again.")
while(True):
    ex2Grade = float(input("  Enter Exam2 grade: "))
    if(ex2Grade>=0 and ex2Grade<=100):
        break
    else:
        print("  Grade must be in range [0..100]. Try again.")
print("")

#MATH
hwAvg = (hw1Grade*10 + hw2Grade*10 + hw3Grade*10) / 3
pjAvg = (pj1Grade + pj2Grade) / 2
exAvg = (ex1Grade + ex2Grade) / 2
semAvg = (hwAvg)*(.30) + (pjAvg)*(.30) + (exAvg)*(.40)

#LTTRGRADE
if(semAvg >= 90 and semAvg <= 100):
    lttrGrade = "A"
if(semAvg >= 80 and semAvg < 90):
    lttrGrade = "B"
if(semAvg >= 70 and semAvg < 80):
    lttrGrade = "C"
if(semAvg >= 60 and semAvg < 70):
    lttrGrade = "D"
if(semAvg >= 0 and semAvg < 60):
    lttrGrade = "F"

#FORMAT
hwAvg = format(hwAvg, ".2f")
pjAvg = format(pjAvg, ".2f")
exAvg = format(exAvg, ".2f")
semAvg = format(semAvg, ".2f")

#REPORT
print("Grade report for: ", name, sep="")
print("  Homework average (30'%' of grade): ", hwAvg, sep="")
print("  Project average (30'%' of grade): ", pjAvg, sep="")
print("  Exam average (40'%' of grade): ", exAvg, sep="")
print("  Student course average: ", semAvg, sep="")
print("  Course grade (CS303E: Spring, 2021): ", lttrGrade, sep="")