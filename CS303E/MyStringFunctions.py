# File: MyStringFunctions.py
# Student: 
# UT EID:
# Course Name: CS303E
# 
# Date Created:
# Date Last Modified: 
# Description of Program: 

def myAppend( str, ch ):
    # Return a new string that is like str but with 
    # character ch added at the end
    return str + ch

def myCount( str, ch ):
    # Return the number of times character ch appears
    # in str.
    count = 0
    for c in str:
      if(c == ch):
        count+=1
    return count

def myExtend( str1, str2 ):
    # Return a new string that contains the elements of
    # str1 followed by the elements of str2, in the same
    # order they appear in str2.
    str3 = str1 + str2
    return str3

def myMin( str ):
    # Return the character in str with the lowest ASCII code.
    # If str is empty, print "Empty string: no min value"
    # and return None.
    mIN = 128
    if( len(str) < 1 ):
        print("Empty string: no min value")
        return None
    else:
        for ch in str :
            if(ord(ch) < mIN):
                mIN = ord(ch)
        return chr(mIN)

def myInsert( str, i, ch ):
    # Return a new string like str except that ch has been
    # inserted at the ith position.  I.e., the string is now
    # one character longer than before. Print "Invalid index" if
    # i is greater than the length of str and return None.
    if( i >= len(str) ):
        print("Invalid index")
        return None
    else:
        strStart = str[0:i]
        strEnd = str[i: ]
        return strStart + ch + strEnd


def myPop( str, i ):
    # Return two results: 
    # 1. a new string that is like str but with the ith 
    #    element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is greater than or 
    # equal to len(str), and return str unchanged and None
    if( i >= len(str) ):
        print("Invalid index")
        return (str, None)
    else:
        strStart = str[ :i]
        strEnd = str[i+1: ]
        ch = str[i]
        nuStr = strStart+strEnd
        return (nuStr, ch)

def myFind( str, ch ):
    # Return the index of the first (leftmost) occurrence of 
    # ch in str, if any.  Return -1 if ch does not occur in str.
    index1 = -1
    a = 0
    for c in str :
        if c == ch:
            index1 = a
            return index1
        else:
            a+=1
    return index1

def myRFind( str, ch ):
    # Return the index of the last (rightmost) occurrence of 
    # ch in str, if any.  Return -1 if ch does not occur in str.
    index2 = -1
    b = 0
    for c in str :
        if c == ch:
            index2 = b
        else:
            b+=1
    return index2


def myRemove( str, ch ):
    # Return a new string with the first occurrence of ch 
    # removed.  If there is none, return str.
    a = 0
    if ch in str: 
        for c in str :
            if c == ch:
                nuStr = str[ :a] + str[a+1: ]
                return nuStr
            else:
                a+=1
    else:
        return str


def myRemoveAll( str, ch ):
    # Return a new string with all occurrences of ch.
    # removed.  If there are none, return str.
    a = 0
    if ch in str: 
        for c in str :
            if c == ch:
                str = str[ :a] + str[a+1: ]
            else:
                a+=1
        return str
    else:
        return str

def myReverse( str ):
    # Return a new string like str but with the characters
    # in the reverse order.
    return str[::-1]