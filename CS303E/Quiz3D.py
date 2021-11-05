# CS 303E Quiz 3D
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

# Problem 1: Fancy Functions
from math import sqrt
def followsRule(num):
    if(num == 0):
        return True
    elif( pow( int(sqrt(num) + 0.5), 2) == num ):
        return True
    else:
        return False

def rangeOfNums(lower, upper):
    count = 0
    for num in range(lower, upper + 1):
        if(followsRule(num)):
            count += 1
    return count

# Problem 2: Phone Class
class Phone:
    def __init__(self, brand, volume=5):
        self.__isMuted = False
        self.__brand = brand
        self.__volume = volume

    def toggleMute(self):
        self.__isMuted = True

    def increaseVolume(self):
        if(self.__volume < 10):
            self.__volume += 1
        return

    def decreaseVolume(self):
        if(self.__volume > 0):
            self.__volume += -1

    def __str__(self):
        if(self.__isMuted):
            return "This "+self.__brand+" phone is currently muted."
        else:
            return "This "+self.__brand+" phone is currently at "+str(self.__volume)+" volume."
