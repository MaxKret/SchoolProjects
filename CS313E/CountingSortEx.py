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
    
    def __str__(self):
        return self.queue


def createQueues():
    '''
    Input: None
    Output: alphaNumQueueList and alphaNumDict, the first containing a list of
    all the queues to use and the second containing a dict of letters and nums as the key and the relative
    index in the queue list as the value
    '''
    alphaNumOrder = "0123456789abcdefghijklmnopqrstuvwxyz"
    alphaNumQueueList = []
    alphaNumDict = {}
    idx = 0
    for char in alphaNumOrder:
        alphaNumDict[char] = idx
        alphaNumQueueList.append(Queue())
        #alphaNumQueueList[alphaNumDict[char]].enqueue(char)
        idx+=1
    
    return alphaNumQueueList, alphaNumDict


def radix_helper_oldest(arr, exp, charPos, alphaNumQueueList, alphaNumDict):

	arrLen = len(arr)

	# The output array elements that will have sorted arr
	output = [0 for x in arr]

	# initialize count array as 0
	count = [0] * (10)

	# Store count of occurrences in count[]
	for i in range(0, arrLen):
		count[int((arr[i] / exp) % 10)] += 1

	# Change count[i] so that count[i] now contains actual
	# position of this digit in output array
	for i in range(1, 10):
		count[i] += count[i - 1]

	# Build the output array
	i = arrLen - 1
	while i >= 0:
		index = int(arr[i] / exp)
		output[count[int(index % 10)] - 1] = arr[i]
		count[int(index % 10)] -= 1
		i -= 1

	# Copying the output array to arr[],
	# so that arr now contains sorted numbers
	i = 0
	for i in range(0, len(arr)):
		arr[i] = output[i]


def radix_helper_old(arr, charPos, alphaNumQueueList, alphaNumDict):
    arrLen = len(arr)
    maybePos = charPos - 1
    charPos = -charPos
    outList = [0 for x in arr]

	# Enqueue each element according to a specified digit
    for i in range(0, arrLen):
        try:
            char = str(arr[i])[charPos]
        except IndexError:
            char = str(arr[i])[0] # or "0" ??
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


def radix_helper(arr, charPos, alphaNumQueueList, alphaNumDict):
    arrLen = len(arr)
    maybePos = charPos - 1
    charPos = -charPos
    outList = [0 for x in arr]

	# Enqueue each element according to a specified digit
    for i in range(0, arrLen):
        try:
            char = str(arr[i])[maybePos]
        except IndexError:
            char = str(arr[i])[-1] # or "0" ??
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


def radix_sort_oldest(a):
    a = [170, 45, 75, 90, 802, 24, 2, 66]
    maxLen = max(len(str(an)) for an in a)
    queueAndDict = createQueues()
    alphaNumQueueList = queueAndDict[0]
    alphaNumDict = queueAndDict[1]
    charPos = 1
    exp = 1
    while maxLen >= charPos:
        radix_helper(a, exp, charPos, alphaNumQueueList, alphaNumDict)
        exp *= 10
        charPos += 1
    return a


# Do counting sort for every digit. Note that instead
# of passing digit number, exp is passed. exp is 10^i
# where i is current digit number
def radix_sort_old(a):
    #a = [170, 45, 75, 90, 802, 24, 2, 66]
    print(a)
    maxLen = max(len(str(an)) for an in a)
    queueAndDict = createQueues()
    alphaNumQueueList = queueAndDict[0]
    alphaNumDict = queueAndDict[1]
    charPos = 1
    while maxLen >= charPos:
        radix_helper(a, charPos, alphaNumQueueList, alphaNumDict)
        print("Pass {}: {}".format(charPos, a))
        charPos += 1
    return a


def radix_sort(a):
    #a = [170, 45, 75, 90, 802, 24, 2, 66]
    print(a) # REMOVE THIS
    maxLen = max(len(str(an)) for an in a)
    queueAndDict = createQueues()
    alphaNumQueueList = queueAndDict[0]
    alphaNumDict = queueAndDict[1]
    charPos = 1
    while maxLen >= charPos:
        radix_helper(a, charPos, alphaNumQueueList, alphaNumDict)
        print("Pass {}: {}".format(charPos, a)) # REMOVE THIS
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
  sorted_list = radix_sort(word_list)

  # print the sorted_list
  print("Expected:")
  print("['42cb3f', '51s23', '520ce8', '720', '7ty2d4', '8fg6d', 'ij9944', 'khbw', 'plaq78d', 'sd67mn9', 'xc65ns3', 'z34']")
  print("Returned:")
  print (sorted_list)

if __name__ == "__main__":
  main()

    
