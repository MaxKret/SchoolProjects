# File: MinMax.py
# Student: Maxwell Kretschmer
# UT EID: mtk739
# Course Name: CS303E
# 
# Date Created: 2/20/21
# Date Last Modified: 2/20/21
# Description of Program: uses a loop and takes a number of user inputted integers and finds the minimum and maximum of the set


#Setup
lastInput = -9999
minIn = 9999
maxIn = -9999
loopBool = True
isEmpty = False


#Loop
while(loopBool):
    #start/input
    curInput = input("Enter an integer or 'stop' to end: ")
    #empty case check
    if curInput == "stop" and lastInput == -9999:
        print("You didn't enter any numbers ")
        isEmpty = True
    #stop check
    if curInput == "stop":
        loopBool = False
    #minmax
    if loopBool:
        curInput=int(curInput)
        if curInput < minIn:
            minIn = curInput
        if curInput > maxIn:
            maxIn = curInput
        #reset/end
    lastInput=curInput

#Print
maxIn=str(maxIn)
minIn=str(minIn)
if not isEmpty:
    print("The maximum is", maxIn)
    print("The minimum is", minIn)