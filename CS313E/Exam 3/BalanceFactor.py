#  File: BalanceFactor.py

#  Description: Determines the balance factor of a binary tree

#  Student Name: Maxwell Kretschmer

#  Student UT EID: mtk739

#  Course Name: CS 313E

#  Unique Number: 86610


class Node (object):
  def __init__ (self, data = None, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right


class Tree (object):
    def __init__ (self):
      self.root = Node()


# Returns the height of the tree
def get_height (aNode):
    '''
    driver for get_heights recursive function
    '''
    lengths = [0]
    if aNode.data != None:
        get_height_helper(aNode, 0, lengths)
    return max(lengths)


def get_height_helper(aNode, pathLength, lengths):
    '''
    recursively checks each path, tracking its len along the way
    returns all path lengths
    '''
    # leaf node found, end of path
    if aNode == None:
        lengths.append(pathLength)
    # continue traversal 
    else:
        pathLength += 1
        get_height_helper(aNode.left, pathLength, lengths)
        get_height_helper(aNode.right, pathLength, lengths)

# Return the integer balance factor of a tree rooted at the given node.    
def balance_factor(node):
  if node != None:
    l = get_height(node.left) if node.left else 0
    r = get_height(node.right) if node.right else 0
    return r - l

  else:
    return 0


# ------ DO NOT CHANGE BELOW HERE ------ #
import pickle
import sys


def main():
    data_in = ''.join(sys.stdin.readlines())
    node = pickle.loads(str.encode(data_in))

    print(balance_factor(node))

if __name__ == "__main__":
    main()
