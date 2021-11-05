# CS 303E Exam 2C
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

# Problem 1: OrgPosition Class
class OrgPosition:
    def __init__(self, name, rank, leadershipPositions):
        # replace pass with your solution to problem 1 here
        self.__name = name
        self.__rank = rank
        self.__leadershipPositions = leadershipPositions

    def updateRanking(self, rank):
        # replace pass with your solution to problem 1 here
        self.__rank = rank

    def numPositions(self):
        # replace pass with your solution to problem 1 here
        return len(self.__leadershipPositions)

    def getLikelyPosition(self):
        # replace pass with your solution to problem 1 here
        if self.__rank > len(self.__leadershipPositions):
            return None
        else:
            return self.__leadershipPositions[(self.__rank) - 1]

    def __str__(self):
        # replace pass with your solution to problem 1 here
        return str(self.__name) + " is ranked number "+ str(self.__rank) +" in the organization"


# Problem 2: Subtract Corresponding Elements
def subtractLists(lst1, lst2):
    # replace pass with your solution to problem 2 here
    lst3 = []
    i = 0
    if len(lst1) >= 1:
        for item in lst1:
            lst3.append( item - lst2[i])
            i+=1
        return lst3
    else:
        return []


# Problem 3: Smaller Letter
def smallerLetter(string):
    # replace pass with your solution to problem 3 here
    i = 0
    result=""
    for i in range(0, len(string), 2):
        if(string[i] <= string[i+1]):
            result += (str(string[i])+str(string[i]))
        else:
            result += (str(string[i+1])+str(string[i+1]))
    return result

# Problem 4: String List to Dictionary
def stringListToDictionary(s):
    # replace pass with your solution to problem 4 here
    outDictionary = {}
    for stringL in s:
        before = ""
        after = ""
        indexDash = stringL.find("-")
        for charL in stringL:
            if( stringL.find(charL) != -1 and stringL.find(charL) < indexDash):
                before += charL
            if(stringL.find(charL) != -1 and stringL.find(charL) > indexDash):
                after += charL
        outDictionary[before] = after

    return outDictionary



# Problem 5: Set of Common Characters
def commonCharacters(tup):
    # replace pass with your solution to problem 5 here
    compTup = tuple()
    compList = []
    outSet = set()
    # 1 STRING CASE
    if len(tup) == 1:
        compTup = tup[0] & tup[0]
        for char in compTup:
            outSet.add(char)
    # MULTIPLE STRINGS CASE
    elif len(tup) > 1:
        #STEPTHRU EA STR IN TUPLE
        for i in range(0, len(tup)):
            compTup = tuple()
            if i <= len(tup) - 2:
                compTup = tup[i] & tup[i+1]
                compList.append(compTup)
            

    return outSet



# Problem 6: Multiple Appearance List
def multipleAppearanceList(lst):
    # replace pass with your solution to problem 6 here 
    lstR = []
    for i in lst:
        if lst.count(i) >= 2:
            lstR.append(i)
    return lstR


# Problem 7: Lagging Lowercase
def laggingLowercase(string):
    # replace pass with your solution to problem 7 here
    if len(string) < 1:
        return string
    if len(string) == 1:
        if(string.isalpha() and string.islower()):
            newCharNum = ord(string) - 1
            if(newCharNum < 97):
                newCharNum = 122
            if(newCharNum > 122):
                newCharNum = 97
            newChar = chr(newCharNum)
            return newChar
        else:
            return string
    else:
        if(string[0].isalpha() and string[0].islower()):
            newCharNum = ord(string[0]) - 1
            if(newCharNum < 97):
                newCharNum = 122
            if(newCharNum > 122):
                newCharNum = 97
            newChar = chr(newCharNum)
            return newChar + laggingLowercase(string[1:])
        else:
            return string[0] + laggingLowercase(string[1:])   


# Problem 8: Set of Small Integers
import math
def smallNumbers(lst):
    # replace pass with your solution to problem 8 here
    if(lst == []):
        return set(lst)
    if len(lst) <= 1:
        if abs(lst[0]) < 20:
            return set([lst[0]])
        else:
            return set()
    else:
        if abs(lst[0]) < 20:
            return set([lst[0]]).union(smallNumbers(lst[1:]))
        else:
            return set().union(smallNumbers(lst[1:]))


if __name__ == "__main__":
    """
    If you want to test your code on your computer, uncomment the respective
    function call(s) below.

    DO NOT CALL YOUR FUNCTIONS ANYWHERE OUTSIDE OF THIS AREA
    """
    #s = OrgPosition('Sarah', 3, ['president', 'vice president', 'treasurer', 'secretary', 'social media manager'])
    #s.updateRanking(4)
    #print(str(s))
    #s = OrgPosition('Sarah', 3, ['president', 'vice president', 'treasurer', 'secretary', 'social media manager'])
    #print(s.numPositions())
    #print(s.getLikelyPosition())
    #b = OrgPosition('Bart', 2, ['CEO'])
    #print(b.numPositions())
    #print(b.getLikelyPosition())
    #print(str(b))

    #print(subtractLists([4, 5, 6], [1, 2, 3]))
    #print(subtractLists([], []))
    #print(subtractLists([1, 2, 3], [-1, -2, -3]))

    #print(smallerLetter('aacdfythoopyqt'))
    #print(smallerLetter(''))
    #print(smallerLetter('nnooppee'))

    #print(stringListToDictionary(['1-2', '33-44', '555-666']))
    #print(stringListToDictionary([]))
    #print(stringListToDictionary(['-', 'd-z']))

    #print(commonCharacters(('abcd', 'bcde', 'cdef')))
    #print(commonCharacters(('sooyong',)))
    #print(commonCharacters(('sam', 'kevin', 'sooyong', 'winnie')))

    #print(multipleAppearanceList([1,2,3,4,5]))
    #print(multipleAppearanceList([]))
    #print(multipleAppearanceList([1,1,2,2,3,3]))

    #print(laggingLowercase('aeiou'))
    #print(laggingLowercase(''))
    #print(laggingLowercase('S00y0ng'))

    #print(smallNumbers([1, 2, 3, 4, 5]))
    #print(smallNumbers([]))
    #print(smallNumbers([-21, 10, 20, 30]))

    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT