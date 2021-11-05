# File: Project2.py
# Student: Max Kretschmer
# UT EID: mtk739
# Course Name: CS303E
# 
# Date Created: 4/8/21
# Date Last Modified: 4/12/21
# Description of Program: A substitution cipher class with key private member with get/set and a decrypt and encrypt function.
#a main method loops through a prompt loop asking for 4 commands(changekey, getkey, en/decrypt) or 'quit'.

import random

# A global constant defining the alphabet. 
alphaString = "abcdefghijklmnopqrstuvwxyz"

# You are welcome to use the following two auxiliary functions, or 
# define your own.   You don't need to understand this code at this
# point in the semester. 

def isLegalKey( key ):
    # A key is legal if it has length 26 and contains all letters.
    # from alphaString.
    return ( len(key) == 26 and all( [ ch in key for ch in alphaString ] ) )

def makeRandomKey():
    # A legal random key is a permutation of alphaString.
    lst = list( alphaString )  # Turn string into list of letters
    random.shuffle( lst )    # Shuffle the list randomly
    return ''.join( lst )    # Assemble them back into a string

def findKeyDiff(text1, text2):
    #outputs list with letter distances btwn
    #encrypt: text1=key text2=alpha
    #decrypt: text1=alpha text2=key
    i=0
    keyDiffLst = []
    for c in text1:
        keyDiffLst.append( ord(c)-ord(text2[i]) )
        i+=1
    return keyDiffLst


# There may be some additional auxiliary functions defined here.
# I had several others, mainly used in encrypt and decrypt. 

class SubstitutionCipher:
    def __init__ (self, key = makeRandomKey() ):
        """Create an instance of the cipher with stored key, which
        defaults to random."""
        if(isLegalKey(key)):
            self.__key = key

    # Note that these are the required methods, but you may define
    # additional methods if you need them.  (I didn't need any.)

    def getKey( self ):
        return self.__key

    def setKey( self, newKey ):
        if(isLegalKey(newKey)):
            self.__key = newKey

    def encryptText( self, plaintext ):
        """Return the plaintext encrypted with respect to the stored key."""
        #encrypt: text1=text text2=key
        result = ""
        lstR = list(result)
        text1 = plaintext
        text2 = self.__key
        #encrypt
        keyDiff = findKeyDiff(text2, alphaString) #key, alpha
        for c in text1:
            if(str(c).isalpha()):
                if(ord(c)>=65 and ord(c)<=90): #CAPS
                    lstR.append( chr( ord(c) + keyDiff[ord(c)-65] ) )
                elif(ord(c)>=97 and ord(c)<=122): #LOWER
                    lstR.append( chr( ord(c) + keyDiff[ord(c)-97] ) )
            else:
                lstR.append(c)
        result = ''.join( lstR )
        return result

    def decryptText( self, ciphertext ):
        """Return the ciphertext decrypted with respect to the stored
        key."""
        #decrypt: text1=text text2=key
        result = ""
        lstR = list(result)
        text1 = ciphertext
        text2 = self.__key
        #decrypt
        keyDiff = findKeyDiff(alphaString, text2) #alpha, key
        for c in text1:
            if(str(c).isalpha()):
                if(ord(c)>=65 and ord(c)<=90): #CAPS
                    lstR.append( chr( 65 + text2.find(c.lower()) ) )
                elif(ord(c)>=97 and ord(c)<=122): #LOWER
                    lstR.append( chr( 97 + text2.find(c) ) )
            else:
                lstR.append(c)
        result = ''.join( lstR )
        return result

def main():
    subC1 = SubstitutionCipher()
    _isQuit = False
    _isQuitKey = False

    while(not _isQuit):
        userIn = input("Enter a command (getKey, changeKey, encrypt, decrypt, quit): ").lower()
        
        if(userIn == "quit"): #quit
            print("Thanks for visiting!")
            _isQuit = True
            continue

        elif(userIn == "getkey"): #getkey
            print("  Current cipher key: ", subC1.getKey(), sep="")
            continue

        elif(userIn == "changekey"): #changekey
            _isQuitKey = False
            while(not _isQuitKey):
                userInKey = input("  Enter a valid cipher key, 'random' for a random key, or 'quit' to quit: ").lower()

                if(userInKey == "quit"): #quit
                    _isQuitKey = True
                    continue
                elif(userInKey == "random"): #random
                    subC1.setKey(makeRandomKey())
                    print("    New cipher key: ", subC1.getKey(), sep="")
                    _isQuitKey = True
                    continue
                else:
                    if(isLegalKey(userInKey)): #legal key
                        subC1.setKey(userInKey)
                        print("    New cipher key: ", subC1.getKey(), sep="")
                        _isQuitKey = True
                        continue
                    else: #illegal key
                        print("    Illegal key entered. Try again!")
                        continue

        elif(userIn == "encrypt"): #encrypt
            userInCrypt = input("  Enter a text to encrypt: ")
            print("    The encrypted text is: ", subC1.encryptText(userInCrypt), sep="")
            continue

        elif(userIn == "decrypt"): #decrypt
            userInDeCrypt = input("  Enter a text to decrypt: ")
            print("    The decrypted text is: ", subC1.decryptText(userInDeCrypt), sep="")
            continue

        else: #error
            print("  Command not recognized. Try again!")
            continue
main()