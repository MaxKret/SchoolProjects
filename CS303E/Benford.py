# File: Benford.py
# Student: Max Kretschmer
# UT EID: mtk739
# Course Name: CS303E
# 
# Date Created: 4/21/21
# Date Last Modified: 4/23/21
# Description of Program: Takes pop. data in from a file, stores the unique populations 
# in a set and records the frequency of the first digit of each population, outputting 
# this information into a file
import os.path

def _OutputDataToFile():
    outfile = open("Benford.txt", "w")
    outfile.write("Total number of cities: "+str(totalPopCount)+"\n")
    outfile.write("Unique population counts: "+str(uniquePopCount)+"\n")
    outfile.write("First digit frequency distributions:\n")
    outfile.write("Digit	Count	Percentage"+"\n")
    for i in range(1,10):
        outfile.write(str(i).ljust(5)+"\t"+str(leadDigiDict[str(i)]).ljust(5)+"\t"+format((leadDigiDict[str(i)]/totalPopCount)*100, ".1f")+"\n")
    outfile.close()
    print("Output written to benford.txt")
    return
#MAIN
popSet = set()
leadDigiDict = {str(x):0 for x in range(1,10)}
totalPopCount = 0

pathStr = input("Enter the name of a file of census data: ")
if not os.path.isfile(pathStr):
    print("File does not exist")
else:

    infile = open(pathStr, "r")
    line = infile.readline()
    line = infile.readline()
    while line:#line
        lineLst = line.split("\t")
        if(len(lineLst) >= 3):
            popNum = lineLst[2].strip()
            totalPopCount+=1
        #Add Pop. to Set
        popSet.add(int(popNum))
        #Add 1 to first digit count
        if(popNum[0] in leadDigiDict):
            leadDigiDict[popNum[0]] += 1
        line = infile.readline()
    infile.close()
uniquePopCount = len(popSet)
_OutputDataToFile()

