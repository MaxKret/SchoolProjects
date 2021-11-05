#  File: Average.py

#  Description: Computes the largest moving average of length greater than or equal to k within a list.

#  Student Name:

#  Student UT EID:

#  Course Name: CS 313E

#  Unique Number: 

import sys

# Input: nums is a list of integers, k is the minimum length sub-array allowed
# Output: returns the maximum average value found as well as a list containing the INCLUSIVE slice(s) corresponding to this average
def get_max_average(nums, k):
    # your code here
    return

# do NOT change main, it has been fully completed for you
def main():
    f = sys.stdin
    nums = [int(x.strip()) for x in f.readline().split()]
    k = int(f.readline().strip())

    highest_average, slices = get_max_average(nums, k)
    print(highest_average)
    print('\n'.join([f'{int(indiv_slice[0])} {int(indiv_slice[1])}' for indiv_slice in slices]))

if __name__ == "__main__":
    main()