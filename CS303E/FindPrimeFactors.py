# File: FindPrimeFactors.py
# Student: Maxwell Kretschmer
# UT EID: mtk739
# Course Name: CS303E
# 
# Date Created: 4/8/21
# Date Last Modified: 4/8/21
# Description of Program: Takes in a integer and checks if its a positive composite integer, otherwise returns an error message 
# or just the number if it is prime and positive, and if so its prints the list of prime factors for that number

#Functions
from math import sqrt
def isPrime ( num ):
    # Deal with evens and numbers < 2.
    if ( num < 2 or num % 2 == 0 ):
        return ( num == 2 )
    # See if there are any odd divisors
    # up to the square root of num.
    divisor = 3
    while ( divisor <= sqrt( num )):
        if ( num % divisor == 0 ):
            return False
        else:
            divisor += 2
    return True

def findNextPrime ( num ):
    if ( num < 2 ):
        return 2
    # If (num >= 2 and num is even ), the
    # next prime after num is at least
    # (num - 1) + 2 , which is odd.
    if ( num % 2 == 0):
        num -= 1
    guess = num + 2
    while ( not isPrime ( guess )):
        guess += 2
    return guess

#Main
#
#If the input is 0, exit with a Goodbye message.
#If the input is 1, report that 1 has no prime factorization.
#If the input is negative, report that.
#Finally, if the input is a positive integer greater than 1, print the prime factorization as a list. If the number is a prime, print a list with just that number.
#
print("Find Prime Factors: ")
userIn = 1
while (userIn != 0):
    userIn = int(input("Enter a positive integer (or 0 to stop): "))
    #0 check
    if(userIn == 0):
        print("Goodbye!")
        exit
    #1 check
    if(userIn == 1):
        print("  1 has no prime factorization.\n")
    #negative check
    if(userIn < 0):
        print("  Negative integer entered.  Try again.\n")
    #positive int
    if(userIn > 1):
        num = userIn

        if(isPrime(num)):
            print("  The prime factorization of ", str(userIn), " is: ", [num], "\n", sep="", end="\n")

        else:
            factors = []
            d = 2
            while(num > 1):
                while( num % d == 0):
                    factors.append(d)
                    num = num / d
                d = findNextPrime(d)
            print("  The prime factorization of ", str(userIn), " is: ", factors, "\n", sep="", end="\n")
                