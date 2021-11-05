# CS 303E Exam 1C
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

# Problem 1 - Octagonal Order
def octagonalOrder():
    # replace pass with your solution to problem 1 here
    k = int(input())
    for i in range (1, k+1):
        print( i*((3*i)-2) , end=" ")

# Problem 2 - Stylish Sum
from math import sqrt
def stylishSum():
    # replace pass with your solution to problem 2 here
    k = int(input())
    sum = 0.0
    for i in range (1, k+1):
        sum += ( (sqrt(i)) / ((i+7)*(i+7)) )
    print(format(sum, ".2f"))


# Problem 3 - Affable Average
def affableAverage():
    # replace pass with your solution to problem 3 here
    d = int(input())
    count = 0
    sumAv = 0.0
    for i in range (1, 51):
        if ( i % d == 0):
            sumAv +=i
            count +=1

    if(sumAv == 0.0):
        print(sumAv)
    else:
        print(format(sumAv/count, ".1f"))

# Problem 4 - The Wienni Walkabout
def theWienniWalkabout():
    # replace pass with your solution to problem 4 here
    I = int(input())
    a = int(input())
    prevTerm = 0
    for i in range(1,6):
        if(i==1):
            print(a, end=" ")
            prevTerm = a
            continue
        if(prevTerm > I):
            prevTerm = (3*prevTerm)+3
            print(prevTerm, end=" ")
            continue
        if(prevTerm < I):
            prevTerm = (8*prevTerm)-5
            print(prevTerm, end=" ")
            continue
        if(prevTerm == I):
            prevTerm = (prevTerm-2)*(prevTerm-2)
            print(prevTerm, end=" ")
            continue

# Problem 5 - Coin Conundrum
def coinConundrum(amount, count):
    # replace pass with your solution to problem 5 here
    if not amount <= 0:
        if(amount >= 60):
            amount += -60
            count += 1
            return coinConundrum(amount, count)
        if(amount >= 12):
            amount += -12
            count += 1
            return coinConundrum(amount, count)
        if(amount >= 3):
            amount += -3
            count += 1
            return coinConundrum(amount, count)
        if(amount >= 1):
            amount += -1
            count += 1
            return coinConundrum(amount, count)
    else:
        print(count,amount)
        return

# Problem 6 - Versatile Vowel
def versatileVowel():
    # replace pass with your solution to problem 6 here
    # A-Z = 65-90  ;  A=65, E=69, I=73, O=79, U=85
    charIn = input()
    charInNum = ord(charIn)
    if(charInNum >= 85 and charInNum <= 90):
        print('U')
    elif(charInNum >= 79):
        print('O')
    elif(charInNum >= 73):
        print('I')
    elif(charInNum >= 69):
        print('E')
    elif(charInNum >= 65):
        print('A')
    
# Problem 7 - Tiered Taxation
def tieredTaxation():
    # replace pass with your solution to problem 7 here
    income = int(input())
    totalTax = 0

    if(income >= 0):
        totalTax += (10000 * 0)
        income += -10000
    if(income <  10000 and income > 0):
        totalTax += (income * 0.10)
        income += -income
    if(income >= 10000 and income > 0):
        totalTax += (10000 * 0.10)
        income += -10000
    if(income >= 0):
        totalTax += (income * 0.20)
        income += -income
    if(income < 0):
        print(0)
    else:
        print(format(totalTax, ".0f"))

# Problem 8 - Opportunistic Operation
def opportunisticOperation():
    # replace pass with your solution to problem 8 here
    x = int(input())
    y = int(input())
    if((x-y) > 100):
        print(format(x/y, ".2f"))
    else:
        print(format(x-y, ".2f"))

if __name__=="__main__":
    """
    If you want to test your code on your computer, uncomment the respective
    function call(s) below.
    
    DO NOT CALL YOUR FUNCTIONS ANYWHERE OUTSIDE OF THIS AREA
    """
    amount = int(input())
    count = 0
    coinConundrum(amount, count)
    #octagonalOrder()
    #stylishSum()
    #affableAverage()
    #theWienniWalkabout()
    #coinConundrum()
    #versatileVowel()
    #tieredTaxation()
    #opportunisticOperation()  
    pass