#  File: Intervals.py

#  Description: The program accepts a file and accepts the first line as the 
#  dimensions for a spiral of numbers. The program creates and stores a 
#  generated spiral and takes additional input values to calculate the sum of
#  the adjacent values. The output is printed individually on a new line. 

#  Student Name: Maxwell Kretschmer

#  Student UT EID: mtk739

#  Partner Name: Alice Gee

#  Partner UT EID: ag67642

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 6/09/2021

#  Date Last Modified: 6/10/2021

import sys

# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval

# creates the new interval from two overlapping intervals  
def make_interval(tup1, tup2):
  temp_tup = [0, 0]
  temp_tup[0] = min( [tup1[0], tup2[0]] )
  temp_tup[1] = max( [tup1[1], tup2[1]] )
  return temp_tup

# merges two tuples into the same interval if they have an overlap
def merge_tuples (tuples_list):
  tuples_list.sort()
  store_tuples = []
  outList = [0 for x in range(len(tuples_list))]
  outListIndex = 0
  
  if len(tuples_list) <= 1:
    return tuples_list

  for i in range(1, len(tuples_list)):      # for each tuple
    temp_tup = []
    _isLooping = True
    _isSameIntvl = False

    # comparing values within each interval if in the other interval
    for j in range( tuples_list[i][0], tuples_list[i][1] + 1) :

      if not _isLooping:
        break

      if j in range( tuples_list[i-1][0], tuples_list[i-1][1] + 1 ):
        # creates a temporary tuple to be added 
        temp_tup = make_interval(tuples_list[i-1], tuples_list[i] )
        _isSameIntvl = True

        #if temp_tup not in outList:
        outList[outListIndex] = temp_tup
        tuples_list[i] = tuple(temp_tup)
        tuples_list[i-1] = 0
        _isLooping = False


    # if intervals no longer overlap, move to next interval 
    if not _isSameIntvl:
      outListIndex += 1

  return_list = []

  for item in outList:
    if item == 0:
      outList.remove(0) 
    else:
      return_list.append(tuple(item))
  
            
  return return_list 
        
    #if reached, no overlap found


# Input: tuples_list is a list of tuples of denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval

def sort_by_interval_size (tuples_list):
  sort_tuples = sorted(tuples_list, key = lambda x: abs(x[1] - x[0]))
  return sort_tuples

# Input: no input
# Output: a string denoting all test cases have passed

def test_cases ():
  assert merge_tuples( [(1,2)] ) == [(1,2)]
  # write your own test cases

  assert sort_by_interval_size([(1,3), (4,5)]) == [(4,5), (1,3)]
  # write your own test cases

  return "all test cases passed"

def main():
  #open file intervals.in and read the data and create a list of tuples
  unformatted_inList = sys.stdin.readlines()
  
  # removes unnecessary characters from the entry #unformatted_inList
  inList = [entry.strip("\n").strip() for entry in unformatted_inList]
  
  # sets the number of intervals and removes from list
  num_intervals = inList[0]
  del inList[0]

  # creates a list of tuples
  transition_lst = [line.split(" ") for line in inList]
  store_tuples = [ (int(line[0]), int(line[1])) for line in transition_lst ]

  # merge the list of tuples
  collapsed_tup_list = merge_tuples (store_tuples)

  # sort the list of tuples according to the size of the interval
  size_sorted_tup_list = sort_by_interval_size (collapsed_tup_list)

  # run your test cases
  # print (test_cases())

  # write the output list of tuples from the two functions
  print(collapsed_tup_list)
  print(size_sorted_tup_list)
  #sys.stdout.write(collapsed_tup_list + '\n')
  #sys.stdout.write(size_sorted_tup_list + '\n')

if __name__ == "__main__":
  main()
