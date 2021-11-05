# File: DaysInMonth.py
# Student: Maxwell Kretschmer
# UT EID: mtk739
# Course Name: CS303E
# 
# Date Created: 2/20/21
# Date Last Modified: 2/20/21
# Description of Program: takes an input of year and month, checks to see if the year is a leap year, and then returns the number of days


#User Input
yearIn = int(input("Please enter a year: "))
monthIn = int(input("Please enter a month: "))


#Leap Year check
if yearIn % 4 == 0:
    IsLeapYear = True
elif yearIn % 100 == 0:
    IsLeapYear = False
elif yearIn % 4 == 0:
    IsLeapYear = True
else:
    IsLeapYear = False

#month to days
nDays = 0
if monthIn == 1:
    month = "January"
    nDays = 31
elif monthIn == 2 and IsLeapYear == True:
    month = "February"
    nDays = 29
elif monthIn == 2:
    month = "February"
    nDays = 28
elif monthIn == 3:
    month = "March"
    nDays = 31
elif monthIn == 4:
    month = "April"
    nDays = 30
elif monthIn == 5:
    month = "May"
    nDays = 31
elif monthIn == 6:
    month = "June"
    nDays = 30
elif monthIn == 7:
    month = "July"
    nDays = 31
elif monthIn == 8:
    month = "August"
    nDays = 31
elif monthIn == 9:
    month = "September"
    nDays = 30
elif monthIn == 10:
    month = "October"
    nDays = 31
elif monthIn == 11:
    month = "November"
    nDays = 30
elif monthIn == 12:
    month = "December"
    nDays = 31
else:
    print("invalid month")

#Formatting
yearIn=str(yearIn)
nDays=str(nDays)


#Output
print(month+" "+yearIn+" has "+nDays+" days")