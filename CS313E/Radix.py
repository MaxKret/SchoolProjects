
#  File: Radix.py

#  Description:

#  Student Name: Maxwell Kretschmer

#  Student UT EID: mtk739

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 7/18/21

#  Date Last Modified: 7/19/21

import sys

class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue if empty
  def is_empty (self):
    return (len(self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len(self.queue))


# Input: None
# Output: alphaNumQueueList and alphaNumDict, the first containing a list of
#         all the queues to use and the second containing a dict of letters and nums as the key and the relative
#         index in the queue list as the value
def createQueues():
    alphaNumOrder = "0123456789abcdefghijklmnopqrstuvwxyz"
    alphaNumQueueList = []
    alphaNumDict = {}
    idx = 0
    for char in alphaNumOrder:
        alphaNumDict[char] = idx
        alphaNumQueueList.append(Queue())
        idx+=1
    
    return alphaNumQueueList, alphaNumDict


# Input: takes in the current Array, a charPos representing the position of digit being checked,
#        and the List of Queues and related dictionary
# Output: None; sorts array in place
def radix_helper(arr, charPos, alphaNumQueueList, alphaNumDict):
    arrLen = len(arr)
    charPos = -charPos
    outList = [0 for x in arr]

	# Enqueue each element according to a specified digit
    for i in range(0, arrLen):
        try:
            char = str(arr[i])[charPos]
        except IndexError:
            char = 0 # or "0" or str(arr[i])[0] ??
        alphaNumQueueList[alphaNumDict[char]].enqueue(arr[i])


	# Build the output array
    idx = 0
    for q in alphaNumQueueList:
        if not q.is_empty():
            for arrLen in range(q.size()):
                outList[idx] = q.dequeue()
                idx+=1

    # Copying the output array to arr[]
    for i in range(0, len(arr)):
        arr[i] = outList[i]


# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort(a):
    # Setup
    #a = [170, 45, 75, 90, 802, 24, 2, 66]
    #print(a) # REMOVE THIS
    maxLen = max(len(str(an)) for an in a)
    queueAndDict = createQueues()
    alphaNumQueueList = queueAndDict[0]
    alphaNumDict = queueAndDict[1]
    charPos = 1

    # Main Loop
    while maxLen >= charPos:
        radix_helper(a, charPos, alphaNumQueueList, alphaNumDict)
        #print("Pass {}: {}".format(charPos, a)) # REMOVE THIS
        charPos += 1
    return a


def main():
  # read the number of words in file
  line = sys.stdin.readline()
  line = line.strip()
  num_words = int (line)

  # create a word list
  word_list = []
  for i in range (num_words):
    line = sys.stdin.readline()
    word = line.strip()
    word_list.append (word)

  '''
  # print word_list
  print (word_list)
  '''

  # use radix sort to sort the word_list
  sorted_list = radix_sort (word_list)

  # print the sorted_list
  #print("Expected:")
  #print("['42cb3f', '51s23', '520ce8', '720', '7ty2d4', '8fg6d', 'ij9944', 'khbw', 'plaq78d', 'sd67mn9', 'xc65ns3', 'z34']")
  #print("Returned:")
  print (sorted_list)

if __name__ == "__main__":
  main()

    
