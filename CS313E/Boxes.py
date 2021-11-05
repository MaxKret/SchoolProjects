
#  File: Boxes.py

#  Description:

#  Student Name: Maxwell Kretschmer

#  Student UT EID: mtk739

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 7/6/21

#  Date Last Modified: 7/9/21

import sys


# returns True if box1 fits inside box2
def does_fit (box1, box2):
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])


# generates all subsets of boxes and stores them in all_box_subsets
# box_list: is a list of boxes that have already been sorted
# sub_set: is a list that is the current subset of boxes
# idx: is an index in the list box_list
# all_box_subsets: is a 3-D list that has all the subset of boxes
def sub_sets_boxes (box_list, sub_set, idx, all_box_subsets):
  #FINISHED SUBSET
  if (idx == len(box_list)):
    all_box_subsets.append(sub_set)
    return all_box_subsets
  #CREATING SUBSET
  else:
    tmp_sub_set = sub_set[:]
    sub_set.append(box_list[idx])
    sub_sets_boxes(box_list, sub_set, idx + 1, all_box_subsets)
    sub_sets_boxes(box_list, tmp_sub_set, idx + 1, all_box_subsets)
    return all_box_subsets
  

# goes through all the subset of boxes and only stores the
# largest subsets that nest in the 3-D list all_nesting_boxes
# largest_size: keeps track what the largest subset is
def largest_nesting_subsets (all_box_subsets, largest_size, all_nesting_boxes):
  for idx in range(len(all_box_subsets)):
    #SIZE == LARGEST SIZE
    if does_nest(all_box_subsets[idx]) and len(all_box_subsets[idx]) == largest_size:
      all_nesting_boxes.append(all_box_subsets[idx])

    #SIZE > LARGEST SIZE
    if does_nest(all_box_subsets[idx]) and len(all_box_subsets[idx]) > largest_size:
      largest_size = len(all_box_subsets[idx])
      all_nesting_boxes = []
      all_nesting_boxes.append(all_box_subsets[idx])

  return all_nesting_boxes


def does_nest(sub_set):
  for i in range(1, len(sub_set)):
    if not does_fit(sub_set[i-1], sub_set[i]):
      return False
  return True


def test_cases():
  assert does_fit([2,2,2], [3,3,3]) == True
  return "Test cases passed"

def main():
  # read the number of boxes 
  line = sys.stdin.readline()
  line = line.strip()
  num_boxes = int (line)

  # create an empty list for the boxes
  box_list = []

  # read the boxes from the file
  for i in range (num_boxes):
    line = sys.stdin.readline()
    line = line.strip()
    box = line.split()
    for j in range (len(box)):
      box[j] = int (box[j])
    box.sort()
    box_list.append (box)

  
  # print to make sure that the input was read in correctly
  #print (box_list)
  #print()

  # sort the box list
  box_list.sort()

  # print the box_list to see if it has been sorted.
  #print (box_list)
  #print()

  # create an empty list to hold all subset of boxes
  all_box_subsets = []

  # create a list to hold a single subset of boxes
  sub_set = []
  
  # generate all subsets of boxes and store them in all_box_subsets
  all_box_subsets = sub_sets_boxes (box_list, sub_set, 0, all_box_subsets)

  # all_box_subsets should have a length of 2^n where n is the number
  # of boxes
  
  largest_size = 0

  # go through all the subset of boxes and only store the
  # largest subsets that nest in all_nesting_boxes
  all_nesting_boxes = largest_nesting_subsets (all_box_subsets, largest_size, box_list)

  # print the largest number of boxes that fit
  print(len(all_nesting_boxes[0]))
  # print the number of sets of such boxes
  print(len(all_nesting_boxes))

if __name__ == "__main__":
  main()

