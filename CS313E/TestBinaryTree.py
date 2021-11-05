#  File: TestBinaryTree.py

#  Description: helper methods for the Tree class that we wrote in class. methods added are is_similar, get_level, get_height, and num_nodes

#  Student Name: Maxwell Kretschmer

#  Student UT EID: mtk739

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 8/2/21

#  Date Last Modified: 8/6/21


import sys


class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild


class Tree (object):
    def __init__ (self):
        self.root = Node()
    
    
    # insert data into the tree
    def insert (self, data):
        new_node = Node (data)

        if (self.root.data == None):
            self.root = new_node
            return
        else:
            current = self.root
            parent = self.root
            while (current != None):
                parent = current
                if (data < current.data):
                    current = current.lChild
                else:
                    current = current.rChild

        # found location now insert node
            if (data < parent.data):
                parent.lChild = new_node
            else:
                parent.rChild = new_node


  # search for a node with given data
    def find (self, data):
        current = self.root
        while (current != None) and (current.data != data):
            if (data < current.data):
                current = current.lChild
            else:
                current = current.rChild
        return current


  # in order traversal - left, center, right
    def in_order (self, aNode):
        if (aNode != None):
            self.in_order (aNode.lChild)
            print (aNode.data, end=" ")
            self.in_order (aNode.rChild)
    
    # pre order traversal - center, left, right
    def pre_order (self, aNode):
        if (aNode != None):
            print (aNode.data, end = " ")
            self.pre_order (aNode.lChild)
            self.pre_order (aNode.rChild)


    # Returns true if two binary trees are similar
    def is_similar (self, pNode):
        '''
        driver for is_similar recursive function
        '''
        anode = self.root
        bnode = pNode.root
        return self.is_similar_helper(anode, bnode)


    def is_similar_helper(self, anode, bnode):
        '''
        recursively checks each pair of nodes for similarity
        returns True if trees are similar, False otherwise
        '''
        if anode == None and bnode == None:
            return True 
        if anode == None and bnode != None:
            return False
        elif anode != None and bnode == None:
            return False
        elif anode.data != bnode.data:
            return False
        else:
            return self.is_similar_helper(anode.lChild, bnode.lChild) and self.is_similar_helper(anode.rChild, bnode.rChild)


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
                self.get_level_helper(level_needed, currentLevel + 1, nodes_on_level, aNode.lChild)
                self.get_level_helper(level_needed, currentLevel + 1, nodes_on_level, aNode.rChild)


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
            self.get_height_helper(aNode.lChild, pathLength, lengths)
            self.get_height_helper(aNode.rChild, pathLength, lengths)


    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    def num_nodes (self):
        '''
        driver for num_nodes recursive function
        '''
        numNodes = self.num_nodes_helper(self.root)
        return numNodes
        

    def num_nodes_helper(self, aNode):
        '''
        recursively traverses through each node in the list, adding 1 for the root to the L and R child
        returns number of nodes in tree
        '''
        # leaf node found
        if aNode == None or aNode.data == None:
            return 0
        # continue traversal
        else:
            return 1 + self.num_nodes_helper(aNode.lChild) + self.num_nodes_helper(aNode.rChild) 


def main():
    # inorder, preorder
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree0_input = list (map (int, line)) 	# converts elements into ints
    tree0 = Tree()
    for x in tree0_input:
        tree0.insert(x)


    print("Tree 0:")
    for i in range(tree0.get_height()):
        print(" Level {}: {}".format(i, [x.data for x in tree0.get_level(i)]))


    print("In Order")
    tree0.in_order(tree0.root)
    print()

    print("Pre Order")
    tree0.pre_order(tree0.root)
    print()


    # inorder, preorder
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree0_input = list (map (int, line)) 	# converts elements into ints
    tree0 = Tree()
    for x in tree0_input:
        tree0.insert(x)


    print("Tree 0:")
    for i in range(tree0.get_height()):
        print(" Level {}: {}".format(i, [x.data for x in tree0.get_level(i)]))


    print("In Order")
    tree0.in_order(tree0.root)
    print()

    print("Pre Order")
    tree0.pre_order(tree0.root)
    print()


    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list (map (int, line)) 	# converts elements into ints
    tree1 = Tree()
    for x in tree1_input:
        tree1.insert(x)

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list (map (int, line)) 	# converts elements into ints
    tree2 = Tree()
    for x in tree2_input:
        tree2.insert(x)

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list (map (int, line)) 	# converts elements into ints
    tree3 = Tree()
    for x in tree3_input:
        tree3.insert(x)

    # Test your method is_similar()
    tree1_sim_tree2 = tree1.is_similar(tree2)
    tree1_sim_tree3 = tree1.is_similar(tree3)
    print("Tree1 is similar to Tree2:", str(tree1_sim_tree2))
    print("Tree1 is similar to Tree3:", str(tree1_sim_tree3))
    print()


    # Print the various levels of two of the trees that are different
    if tree1_sim_tree2: # 1 and 3 are diff
        print("Tree 1:")
        for i in range(tree1.get_height()):
            print(" Level {}: {}".format(i, [x.data for x in tree1.get_level(i)]))
        print("Tree 3:")
        for i in range(tree3.get_height()):
            print(" Level {}: {}".format(i, [x.data for x in tree3.get_level(i)]))

    else: # 1 and 2 are diff
        print("Tree 1:")
        for i in range(tree1.get_height()):
            print(" Level {}: {}".format(i, [x.data for x in tree1.get_level(i)]))
        print("Tree 2:")
        for i in range(tree2.get_height()):
            print(" Level {}: {}".format(i,[x.data for x in tree2.get_level(i)]))
    print()


    # Get the height of the two trees that are different
    if tree1_sim_tree2: # 1 and 3 are diff
        print("Tree 1 height:",tree1.get_height())
        print("Tree 3 height:",tree3.get_height())

    else: # 1 and 2 are diff
        print("Tree 1 height:",tree1.get_height())
        print("Tree 2 height:",tree2.get_height())
    print()


    # Get the total number of nodes a binary search tree
    print("Tree 1 has",tree1.num_nodes(), "nodes")
    print("Tree 2 has",tree2.num_nodes(), "nodes")
    print("Tree 3 has",tree3.num_nodes(), "nodes")




if __name__ == "__main__":
  main()