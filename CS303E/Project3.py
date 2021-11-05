# File: Project3.py
# Student: Max Kretschmer
# UT EID: mtk739
# Course Name: CS303E
# 
# Date Created: 5/2/21
# Date Last Modified: 5/3/21
# Description of Program: a query processing system that allows a user to ask questions 
# about the number of cases and deaths in specific counties or statewide. The available commands are:
# help, quit, counties, cases (by county or statewide), and deaths (by county or statewide)
# 
# 
import os.path

# FILE PARSER
def _fileParser(pathStr):
    storDict = {}
    totalConfirmedCases = 0
    totalConfirmedDeaths = 0
    countyList = []
    infile = open(pathStr, "r")
    line = infile.readline()
    while line: # data line
        if "#" not in line:
            lineLst = line.split(",")
            countyName=lineLst[0]
            confirmedCases=int(lineLst[1])
            confirmedDeaths=int(lineLst[3].strip())
            totalConfirmedCases+=confirmedCases
            totalConfirmedDeaths+=confirmedDeaths
            countyList.append(countyName)
            storDict[countyName] = (confirmedCases, confirmedDeaths)
        line = infile.readline()
    storDict["Texas"] = (totalConfirmedCases, totalConfirmedDeaths)
    infile.close()
    return (storDict, countyList)

# MAIN
#  SETUP
pathStr = "county-covid-data.txt"
if not os.path.isfile(pathStr):
    print("File county-covid-data.txt not found.")
    exit
else:
    outList = _fileParser(pathStr)
    casesDict = outList[0]
    countyList = outList[1]
#  WELCOME
    print("Welcome to the Texas Covid Database Dashboard.")
    print("This provides Covid data in Texas as of 1/26/21.")
    print("Creating dictionary from file: county-covid-data.txt")
    print("")
    print("Enter any of the following commands:")
    print("Help - list available commands;")
    print("Quit - exit this dashboard;")
    print("Counties - list all Texas counties;")
    print("Cases <countyName>/Texas - confirmed Covid cases in specified county or statewide;")
    print("Deaths <countyName>/Texas - Covid deaths in specified county or statewide.")
#  COMMAND LOOP
    loopBool = True
    while(loopBool):
        userIn = input("Please enter a command: ").lower()
        #QUIT
        if userIn == "quit":
            print("Thank you for using the Texas Covid Database Dashboard.  Goodbye!")
            loopBool = False
        #HELP
        elif userIn == "help":
            print("Help - list available commands;")
            print("Quit - exit this dashboard;")
            print("Counties - list all Texas counties;")
            print("Cases <countyName>/Texas - confirmed Covid cases in specified county or statewide;")
            print("Deaths <countyName>/Texas - Covid deaths in specified county or statewide.")
        #COUNTIES
        elif userIn == "counties":
            loopCt = 0
            for county in countyList:
                loopCt+=1
                print(county, ", ", sep="", end="")
                if loopCt%10 == 0:
                    print()
            print("\n")
        #CASES
        elif "cases" in userIn:
            countyCaseReq = userIn[6:].title()
            if(countyCaseReq == "Texas"):
                countyCases = casesDict["Texas"][0]
                print("Texas total confirmed Covid cases:", countyCases)
            if(countyCaseReq in casesDict.keys()):
                countyCases = casesDict[countyCaseReq][0]
                print(countyCaseReq, "county has", countyCases, "confirmed Covid cases.")
            else:
                print("County", countyCaseReq, "is not recognized.")
        #DEATHS
        elif "deaths" in userIn:
            countyDeathReq = userIn[6:].title()
            if(countyDeathReq == "Texas"):
                countyDeaths = casesDict["Texas"][1]
                print("Texas total confirmed Covid deaths:", countyDeaths)
            if(countyDeathReq in casesDict.keys()):
                countyDeaths = casesDict[countyDeathReq][1]
                print(countyDeathReq, "county has", countyDeaths, "fatalities.")
            else:
                print("County", countyDeathReq, "is not recognized.")
        #INPUT ERROR
        else:
            print("Command is not recognized.  Try again!")