# File: ComparingLinearBinarySearch.py
# Student: Max Kretschmer
# UT EID: mtk739
# Course Name: CS303E
# 
# Date Created: 4/13/21
# Date Last Modified: 4/16/21
# Description of Program: runs 100,000 tests of a linear search of a random positive int [0,999] in the same shuffled list 
# of nums [0,999] and averages the num of probes/comparisons for each number n of tests(n=10,100,1000,etc). then runs 1,000 tests
# of a binary search of random values [0,999] in an ordered list [0,999] and prints the avg num of probes and 
# compares it to log2n (log2(1000) in this case)
# 

#Given
import random, math
def linearSearch( lst, key ):
    """ Search for key in unsorted list lst.  Note that
        the index + 1 is also the number of probes. """
    for i in range( len(lst) ):
        if key == lst[i]:
            return i
    return -1

def binarySearch( lst, key ):
    """ Search for key in sorted list lst. Return
        a pair containing the index (or -low - 1)
        and a count of number of probes. """
    count = 0
    low = 0
    high = len(lst) - 1
    while (high >= low):
        count += 1
        mid = (low + high) // 2
        if key < lst[mid]:
            high = mid - 1
        elif key == lst[mid]:
            return (mid, count)
        else:
            low = mid + 1
    # Search failed
    return (-low - 1, count)


#Main

#Linear
print("Linear search:")

# 10
numTests = 0
rndList = [x for x in range(1000)]
random.shuffle(rndList)
results = []
sumProbes = 0.0
while(numTests < 10):
    results.append( (linearSearch(rndList, random.randint(0, 999))) + 1) #search and append num of probes to results
    numTests += 1 #count++
for probeNum in results:
    sumProbes += float(probeNum)
avgProbes = sumProbes/10
print("  Tests: ", numTests,"       Average probes: ", format(avgProbes, ".1f"), sep="")

# 100
numTests = 0
results = []
sumProbes = 0.0
while(numTests < 100):
    results.append( (linearSearch(rndList, random.randint(0, 999))) + 1) #search and append num of probes to results
    numTests += 1 #count++
for probeNum in results:
    sumProbes += float(probeNum)
avgProbes = sumProbes/100
print("  Tests: ", numTests,"      Average probes: ", format(avgProbes, ".2f"), sep="")

# 1000
numTests = 0
results = []
sumProbes = 0.0
while(numTests < 1000):
    results.append( (linearSearch(rndList, random.randint(0, 999))) + 1) #search and append num of probes to results
    numTests += 1 #count++
for probeNum in results:
    sumProbes += float(probeNum)
avgProbes = sumProbes/1000
print("  Tests: ", numTests,"     Average probes: ", format(avgProbes, ".3f"), sep="")

# 10000
numTests = 0
results = []
sumProbes = 0.0
while(numTests < 10000):
    results.append( (linearSearch(rndList, random.randint(0, 999))) + 1) #search and append num of probes to results
    numTests += 1 #count++
for probeNum in results:
    sumProbes += float(probeNum)
avgProbes = sumProbes/10000
print("  Tests: ", numTests,"    Average probes: ", format(avgProbes, ".4f"), sep="")

#100000
numTests = 0
results = []
sumProbes = 0.0
while(numTests < 100000):
    results.append( (linearSearch(rndList, random.randint(0, 999))) + 1) #search and append num of probes to results
    numTests += 1 #count++
for probeNum in results:
    sumProbes += float(probeNum)
avgProbes = sumProbes/100000
print("  Tests: ", numTests,"   Average probes: ", format(avgProbes, ".5f"), sep="")


#Binary
print("Binary search:")
avgProbes = 0.0
numTests = 0
lst999 = [x for x in range(1000)]
results = []
sumProbes = 0.0
while(numTests < 1000):
    results.append( binarySearch(rndList, random.randint(0, 999)) ) #search and append num of probes to results
    numTests += 1 #count++
for probeNum in results:
    sumProbes += float(probeNum[1])
avgProbes = sumProbes/1000
logDiff = abs(9.96578428466 - avgProbes)
print("  Average number of probes: ", format(avgProbes, ".3f"), sep="")
print("  Differs from log2(1000) by: ", logDiff, sep="") 