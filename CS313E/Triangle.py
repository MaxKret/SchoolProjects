
#  File: Triangle.py

#  Description:  find the greatest path sum starting at the top of the triangle and moving only to adjacent numbers on the row below.

#  Student Name: Max Kretschmer

#  Student UT EID: mtk739

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 7/11/21

#  Date Last Modified: 7/12/21

import sys

from timeit import timeit

# returns the greatest path sum using exhaustive search (RECURSIVE)
def brute_force (grid):
  all_path_sums = []
  brute_force_helper(grid, 0, 0, all_path_sums, 0)
  return max(all_path_sums)

def brute_force_helper (grid, col, row, all_path_sums, current_path_sum):
  if row == (len(grid)):
    all_path_sums.append(current_path_sum)
  else: 
    current_path_sum += grid[row][col]
    return brute_force_helper(grid, col, row + 1, all_path_sums, current_path_sum) or brute_force_helper(grid, col + 1, row + 1, all_path_sums, current_path_sum)


# returns the greatest path sum using greedy approach (LINEAR)
def greedy (grid):
  sum=0
  last_col = 0
  for row in range(len(grid)):
    #TOP OF TRIANGLE
    if row == 0:
      sum += grid[0][0]
    #REST OF TRIANGLE
    else:
      if grid[row][last_col] > grid[row][last_col+1]:
        sum += grid[row][last_col]
      else:
        sum += grid[row][last_col+1]
        last_col += 1
  return sum


# returns the greatest path sum using divide and conquer approach (RECURSIVE)
def divide_conquer (grid):
  if len(grid) == 1:
    return grid[0][0]
  else:
    return grid[0][0] + max(divide_conquer(create_triangle(grid, grid[1][0])), divide_conquer(create_triangle(grid, grid[1][1])))


# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
  for i in range(len(grid)-2, -1, -1):
    for j in range(i+1):
      if (grid[i+1][j] > grid[i+1][j+1]):
        grid[i][j] += grid[i+1][j]
      else:
        grid[i][j] += grid[i+1][j+1]
  return grid[0][0]



#Creates new triangle grid
def create_triangle(grid, start):
  '''
  Creates new triangle using an existing triangle and a start number
  '''
  n = len(grid[-1])-1
  new_grid = [[0 for i in range (n)] for j in range (n)]
  top, left_bound = tri_find(grid, start)
  right_bound = left_bound + 0
  i=0
  for row in range(top, len(grid)):
    j = 0
    for col in range(left_bound, n+1):
      if grid[row][col] == 0:
        break
      if col <= right_bound:
        new_grid[i][j] = grid[row][col]
        j+=1
    i+=1
    right_bound += 1
  return new_grid



def tri_find(grid, value):
  '''
  finds value in grid, not including the top value
  '''
  idx = 0
  for row in grid:
    try:
      if grid.index(row) != 0:
        return (grid.index(row), row.index(value))
    except ValueError:
      continue




# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  # read number of lines
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create an empty grid with 0's
  grid = [[0 for i in range (n)] for j in range (n)]

  # read each line in the input file and add to the grid
  for i in range (n):
    line = sys.stdin.readline()
    line = line.strip()
    row = line.split()
    row = list (map (int, row))
    for j in range (len(row)):
      grid[i][j] = grid[i][j] + row[j]

  return grid 

def main ():
  # read triangular grid from file
  grid = read_file()
  
  
  # check that the grid was read in properly
  #print (grid)

  #TEST CREATE_TRIANGLE
  left_grid = create_triangle(grid, 7)
  right_grid = create_triangle(grid, 4)


  # output greatest path from exhaustive search
  print("The greatest path sum through exhaustive search is ")
  print("{}".format(brute_force(grid)))

  # print time taken using exhaustive search
  times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
  times = times / 10
  print("The time taken for exhaustive search in seconds is")
  print("{:f}".format(times), end="\n\n")


  # output greatest path from greedy approach
  print("The greatest path sum through greedy search is ")
  print("{}".format(greedy(grid)))

  # print time taken using greedy approach
  times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
  times = times / 10
  print("The time taken for greedy approach in seconds is")
  print("{:f}".format(times), end="\n\n")


  # output greatest path from divide-and-conquer approach
  print("The greatest path sum through recursive search is ")
  print("{}".format(divide_conquer(grid)))

  # print time taken using divide-and-conquer approach
  times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
  times = times / 10
  print("The time taken for recursive search in seconds is")
  print("{:f}".format(times), end="\n\n")


  # output greatest path from dynamic programming 
  print("The greatest path sum through dynamic programming is ")
  print("{}".format(dynamic_prog(grid)))

  # print time taken using dynamic programming
  times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
  times = times / 10
  print("The time taken for dynamic programming in seconds is")
  print("{:f}".format(times))


if __name__ == "__main__":
  main()

