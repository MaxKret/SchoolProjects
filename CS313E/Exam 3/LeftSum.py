#  File: LeftSum.py

#  Description: Get the left sum of the BST

#  Student Name: Maxwell Kretschmer

#  Student UT EID: mtk739

#  Course Name: CS 313E

#  Unique Number: 86610


import sys
from typing import DefaultDict

class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return (self.queue.pop(0))

    # check if the queue is empty
    def is_empty(self):
        return (len(self.queue) == 0)

    # return the size of the queue
    def size(self):
        return (len(self.queue))

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):
  def __init__ (self):
    self.root = None

  # insert data into the tree
  def insert (self, data):
    new_node = Node (data)

    if (self.root == None):
      self.root = new_node
      return
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (data < current.data):
          current = current.lchild
        else:
          current = current.rchild

      # found location now insert node
      if (data < parent.data):
        parent.lchild = new_node
      else:
        parent.rchild = new_node

  # ***There is no reason to change anything above this line***


  # Returns an integer for the left sum of the BST
  def get_left_sum(self):
    left_sum = 0

    for i in range(self.get_height()):
      tree_level = self.get_level(i)
      left_sum += tree_level[0].data

    return left_sum



# Returns a list of nodes at a given level from left to right
  def get_level(self, level):
    '''
    driver for get_level recursive function
    '''
    nodes_on_level = []
    if self.root.data != None:
        self.get_level_helper(level, 0, nodes_on_level, self.root)
    return nodes_on_level
    

  def get_level_helper(self, level_needed, currentLevel, nodes_on_level, aNode):
      '''
      recursively checks each level for the specified one, appending the data into 'nodes_on_level'
      returns None but alters the 'nodes_on_level' within get_level()
      '''
      if currentLevel > level_needed:
          return
      if aNode == None:
          return

      else:
          #edge case: level found
          if currentLevel == level_needed:
              if aNode.data != None:
                  nodes_on_level.append(aNode)

          # level not found, continue traversal
          else:
              self.get_level_helper(level_needed, currentLevel + 1, nodes_on_level, aNode.lchild)
              self.get_level_helper(level_needed, currentLevel + 1, nodes_on_level, aNode.rchild)


  # Returns the height of the tree
  def get_height (self):
      '''
      driver for get_heights recursive function
      '''
      lengths = [0]
      if self.root.data != None:
          self.get_height_helper(self.root, 0, lengths)
      return max(lengths)


  def get_height_helper(self, aNode, pathLength, lengths):
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
          self.get_height_helper(aNode.lchild, pathLength, lengths)
          self.get_height_helper(aNode.rchild, pathLength, lengths)



# ***There is no reason to change anything below this line***

def main():
    # Create tree
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree_input = list (map (int, line))    # converts elements into ints

    tree = Tree()
    for i in tree_input:
      tree.insert(i)

    print(tree.get_left_sum())

if __name__ == "__main__":
  main()