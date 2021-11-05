# File: EasterSunday.py
# Student: Maxwell Kretschmer
# UT EID: mtk739
# Course Name: CS303E
# 
# Date Created: 2/1
# Date Last Modified: 2/1
# Description of Program: Takes an input of a year integer, performs multiple interger divisions to find quotients and modulo to find remainders with Gauss' algorithm, in order to find the month and day in which easter sunday falls on that year. 
#
#User Prompt
#year = input("Enter year: ")
year0 = int(2000)
def easterSunday(year):
    year = int(year)
    #Variable Init
    y = year
    a = y%19
    b = y//100
    c = y%100
    d = b//4
    e = b%4
    g = (8 * b + 13)//25
    h = (19 * a + b - d - g + 15) % 30
    j = c//4
    k = c%4
    m = (a + 11 * h) // 319
    r = (2 * e + 2 * j - k - h + m + 32) % 7
    n = (h - m + r + 90) // 25
    p = (h - m + r + n + 19) % 32
    #Print results
    month=str(n)
    day=str(p)
    year=str(year)
    print("In "+ year +" Easter Sunday is on month "+month+" and day "+ day)
limit = 2020
while (year0 <= limit):
    easterSunday(year0)
    year0+=1