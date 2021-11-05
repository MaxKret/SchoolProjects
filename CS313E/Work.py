
#  File: Work.py

#  Description:

#  Student Name: Maxwell Kretschmer

#  Student UT EID: mtk739

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 7/1/21

#  Date Last Modified: 7/2/21

import sys

import time

# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of each term in the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series = num lines before falling asleep
def sum_series (v, k):
  sumSeries = 0.0
  ct = 0
  term = v
  while term > 0:
    term = v // (k**ct)
    sumSeries += term
    ct += 1
  return sumSeries

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):
  '''
  (1 ≤ n ≤ 10^6)
  (2 ≤ k ≤ 10)

  def sequential_search (a, x):
  for i in range (len(a)):
    if (a[i] == x):
      return i
  return -1
  
  n = Vmax
  k = prod factor
  a = list -> sum_series 
  x = value to find
  a[i]==x -> sum_series(v,k) >= n(or Vmax)
  '''
  #V: 1 -> numLines + 1 ; v can't be 0 lines
  for v in range (1, n+1):
    if(sum_series(v,k) >= n):
      return v
  return -1

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search (n, k):
  '''
  (1 ≤ n ≤ 10^6)
  (2 ≤ k ≤ 10)

  def binary_search (a, x):
  lo = 0
  hi = len(a) - 1
  while (lo <= hi):
    mid = (lo + hi) // 2
    if (x > a[mid]):
      lo = mid + 1
    elif (x < a[mid]):
      hi = mid - 1
    else:
      return mid
  return -1

  n = Vmax
  k = prod factor
  a = list -> sum_series 
  x = value to find - > min v
  '''
  lo = 0
  hi = n
  while (lo <= hi):
    v = (lo + hi) // 2
    #v = mid
    if (n > sum_series(v,k)):
      #V is TOO LOW
      lo = v + 1
    elif (n < sum_series(v,k)):
      #V is TOO HIGH
        hi = v - 1
    else:
      return v
  return v

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases
  assert linear_search(300, 10) == binary_search(300, 10)

  return "all test cases passed"

def main():
  # read number of cases
  line = sys.stdin.readline()
  line = line.strip()
  num_cases = int (line)

  for i in range (num_cases):
    line = sys.stdin.readline()
    line = line.strip()
    inp =  line.split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    sys.stdout.write("Binary Search: " + str(binary_search(n, k)) + "\n")
    finish = time.time()
    sys.stdout.write("Time: " + "{}".format(finish - start) + "\n")

    sys.stdout.write("\n")

    start = time.time()
    sys.stdout.write("Linear Search: " + str(linear_search(n, k)) + "\n")
    finish = time.time()
    sys.stdout.write("Time: " + "{}".format(finish - start) + "\n")

    sys.stdout.write("\n")
    sys.stdout.write("\n")

if __name__ == "__main__":
  main()

