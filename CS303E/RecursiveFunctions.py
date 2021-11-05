# File: RecursiveFunctions.py
# Student: 
# UT EID:
# Course Name: CS303E
# 
# Date Created:
# Date Last Modified: 
# Description of Program: 
#

def sumItemsInList( L ):
    """ Given a list of numbers, return the sum. """
    if L == []:
        return 0
    else:
        return L[0] + sumItemsInList( L[1:] )

def countOccurrencesInList( key, L ):
    """ Return the number of times key occurs in 
    list L. """
    if L == []:
        return 0
    elif key == L[0]:
        return 1 + countOccurrencesInList( key, L[1:] )
    else:
        return countOccurrencesInList( key, L[1:] )

def addToN ( n ):
    if n == 0:
        return 0
    else:
        return n + addToN(n-1)

def findSumOfDigits( n ):
    """ Return the sum of the digits in a non-negative integer. """
    if(n < 10):
        return n
    else:
        return n%10 + findSumOfDigits(n//10)
def decimalToBinary( n ):
    """ Given a nonnegative decimal integer n, return the 
    binary representation as a string. """
    if(n <= 1):
        return str(n)
    else:
        return str(decimalToBinary(n // 2)) + str(n % 2)

def decimalToList( n ):
    """ Given a positive decimal integer, return a list of the 
    digits (as strings). """
    if n < 10:
        return [n]
    return decimalToList(n//10) + [n%10]

def isPalindrome( s ):
    """ Return True if string s is a palindrome and False
    otherwise. Count the empty string as a palindrome. """
    if(len(s) <= 1):
        return True
    if(s[0] != s[len(s)-1]):
       return False
    else:
        return isPalindrome(s[1:len(s)-1])

def findFirstUppercase( s ):
    """ Return the first uppercase letter in 
    string s, if any.  Return None if there is none. """
    if(findFirstUppercaseIndex(s) == -1):
        return None
    else:
        return s[findFirstUppercaseIndex(s)]


def findFirstUppercaseIndexHelper( s, index ):
    """ *Recursive* Helper function for findFirstUppercaseIndex. """
    firstUpperIndex = -1
    #Failure Base Case
    if(index >= len(s)):
        return firstUpperIndex
    #Success Base Case
    if(ord(s[index]) >= 65 and ord(s[index]) <= 90 ):#UPPERCASE
        firstUpperIndex = index
        return firstUpperIndex
    #Recrusive
    if((ord(s[index]) >= 97 and ord(s[index]) <= 122) or ord(s[index]) == 32):#LOWERCASE or SPACE
        return findFirstUppercaseIndexHelper(s, index+1)
    


# The following function is already completed for you.  But 
# make sure you understand what it's doing. 

def findFirstUppercaseIndex( s ):
    """ Return the index of the first uppercase letter in 
    string s, if any.  Return -1 if there is none.  This one 
    requires a helper function, which is the recursive function. """
    return findFirstUppercaseIndexHelper( s, 0 )

