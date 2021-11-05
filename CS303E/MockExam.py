# CS 303E Mock Exam (homework 6)
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

# Problem 1: Sphere Surface Area
import math
def sphereSurfaceArea():
    # write your solution to problem 1 here
    rad = float(input())
    if(rad < 0):
        print("Negative radius entered")
        return
    surfAreaSphere = 4.0 * math.pi * math.pow(rad, 2)
    print(format(surfAreaSphere, ".2f"))



# Problem 2: Make Uppercase
def makeUppercase():
    # write your solution to problem 2 here
    charIn = input()
    if(ord(charIn) < 123 and ord(charIn) > 96):
        print( chr( ord(charIn) - 32 ) )
    else:
        print(charIn)



# Problem 3: Sum Series
def sumSeries():
    # write your solution to problem 3 here
    n = int(input())
    sumSer = 0
    i = 1
    j = i + 1
    while(i < n):
        sumSer += (i * j)
        i+=1
        j+=1
    print(sumSer)



# Problem 4: Sort Three Integers
def sortThreeIntegers():
    # write your solution to problem 4 here
    inOne = input()
    inTwo = input()
    inThree = input()
    minIn = int(inOne)
    medIn = int(inTwo)
    maxIn = int(inThree)
    i = 0
    while(i < 3):
        if(minIn > medIn):
            tempIn = medIn
            medIn = minIn
            minIn = tempIn
        if(medIn > maxIn):
            tempIn = maxIn
            maxIn = medIn
            medIn = tempIn
        i+=1
    print(minIn, medIn, maxIn)


# Problem 5: Sum Positive Floats
def sumPositiveFloats():
    # write your solution to problem 5 here
    userIn = 1
    sumPos = 0.0
    while(userIn != 0):
        userIn = float(input())
        if(userIn > 0):
            sumPos += userIn
    print(format(sumPos, ".3f"))
            



# Problem 6: Print Squared Table
def printSquaredTable():
    # write your solution to problem 6 here
    maxIn = int(input())
    n = 1
    print("  n      n**2")
    print("-------------")
    while(n <= maxIn):
        print(format(n, "3d"), format(n*n, ">10d"), sep="")
        n+=1




# Problem 7: Largest Square
def largestSquare():
    # write your solution to problem 7 here
    n = int(input())
    k = 0
    while( (k+1)*(k+1) <= n):
        k+=1
    print(k)



# Problem 8: Collatz Conjecture
def collatzConjecture():
    # write your solution to problem 8 here
    n = int(input())
    currTerm = 0
    prevTerm = n
    count = 1
    if(n == 1):
        print(n)
        return
    while(currTerm != 1):
        if(prevTerm % 2 == 0): #is even
            currTerm = prevTerm/2
            prevTerm = currTerm
            count+=1
        elif(prevTerm % 2 == 1): #is oddd
            currTerm = (prevTerm*3) + 1
            prevTerm = currTerm
            count+=1
    print(count)
