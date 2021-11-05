#  File: reward.py

#  Description: The ABC staff decides to find the minimum number of gifts as each customer's reward.

#  Student Name: Maxwell Kretschmer

#  Student UT EID: mtk739

#  Course Name: CS 313E

#  Unique Number: 86610

import sys

max_val = 1000

def getmin(prices, T):
	# (1) Compute 10% of the reward, where N is the reward: N = 10% of T (1 line)
	
	
	# table[i] will be storing the minimum
	# number of gifts required for i value.
	table = [0 for i in range(N + 1)]

	# Base case (If given value N is 0)
	table[0] = 0

	# Initialize all table values as max_val
	for i in range(1, N + 1):
		table[i] = max_val

	# Look at one gift's price at a time
	# Fill out the table from 1 to N
	# Update the table with the min # of gifts
	for p in range(len(prices)):
		for i in range(1, N+1): 
			if(i >= prices[p]): 
				# (2) Update the DP: table[i] = ... (1 line)
				print("prices, i = ", prices[p], i, table)
				
	# (3) If you cannot find the result, return -1 (2 lines)
	
	
	return table[N]


if __name__ == "__main__":

	# Read input list of prices for each gift
	prices_str = sys.stdin.readline().split()
	prices = [ int(x) for x in prices_str ]

	# Read total price that the customer spends
	T = int(sys.stdin.readline())

	print(getmin(prices, T))

