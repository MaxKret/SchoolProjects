#  File: InterestingDrink.py

#  Description: Implement find_purchase_options function that given a list of integers named prices that contains
#               the price of black tea in each store, and a list of integers named money that contains the amount of money
#               Tim will spend in a given day, returns a list of integers representing how many different shops
#               Tim can buy a cup of black tea.

#  Student Name:

#  Student UT EID:

#  Course Name: CS 313E

#  Unique Number:

import sys

#BINARY SEARCH IMPLMT
#Returns: Idx of Element
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

# Input: prices a list of integers containing the price of black tea in each store
#        money  a list of integers containing the amount of money Tim will spend in a given day
# Returns: a list of integers representing how many different shops Tim can buy a cup of black tea.
def find_purchase_options(prices, money):
    #SETUP
    dayCounter = 0
    option_list = [0 for x in money]
    sorted_prices = sorted(prices)
    value = 0

    #CHECK MONEY EACH DAY
    for daysMoney in money:
        #EDGE CASES
        if daysMoney >= sorted_prices[-1]:
            option_list[dayCounter] = len(sorted_prices)
            dayCounter += 1
            continue
        if daysMoney < sorted_prices[0]:
            option_list[dayCounter] = 0
            dayCounter += 1
            continue
        #BINARY SEARCH FOR VAL IN PRICES
        searchReturn = -1
        value = daysMoney
        while searchReturn == -1:
            searchReturn = binary_search(sorted_prices, value)
            if (value > 0) and (searchReturn == -1):
                value -= 1
            else:
                break
        #APPEND NUM OF OPTIONS TO OPTIONS LIST
        if searchReturn >= 0:
            #CHECK FOR DUPLICATE VALUES HIGHER IN LIST
            if searchReturn+1 < len(sorted_prices):
                while sorted_prices[searchReturn] == sorted_prices[searchReturn+1]:
                    if sorted_prices[searchReturn] == sorted_prices[searchReturn+1]:
                        searchReturn+=1
            #RETURN FINAL IDX+1 TO GIVE LEN OF PRICES AVAIL
            option_list[dayCounter] = 1+searchReturn
        else:
            #NO IDX FOUND
            option_list[dayCounter] = 0
        dayCounter += 1
    return option_list


#######################################################################################################
# No need to change the main()
# The input format the the main is two lines, each line contains some integers split by a single space.
# For example:
# 3 10 8 6 11
# 1 10 3 11
#######################################################################################################
def main():
    # Read the prices list
    prices = [*map(int, sys.stdin.readline().split())]
    # Read the money list
    money = [*map(int, sys.stdin.readline().split())]
    # print the answer
    ans = find_purchase_options(prices, money)
    sys.stdout.write(f'Result by calling find_purchase_option {ans}')


if __name__ == '__main__':
    main()
