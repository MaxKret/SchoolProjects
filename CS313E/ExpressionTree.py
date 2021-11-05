#  File: ExpressionTree.py

#  Description:

#  Student Name: Maxwell Kretschmer

#  Student UT EID: mtk739

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 8/1/21

#  Date Last Modified: 8/2/21

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']


class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild


class Tree (object):
    def __init__ (self):
        self.root = Node()
    

    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree (self, expr):
        # initialize tokens, stack, and node pointer
        tokens = expr.split()
        stack = Stack()
        current_node = self.root

        # parsing
        for token in tokens:

            # left paren - start an expr
            if token == '(':
                # push current node
                stack.push(current_node)
                # create and move to a lChild
                current_node.lChild = Node()
                current_node = current_node.lChild

            # operator
            elif token in operators:
                # assign data and push current node
                current_node.data = token
                stack.push(current_node)
                # create and move to a rChild
                current_node.rChild = Node()
                current_node = current_node.rChild

            # operand
            elif token.isdigit() or '.' in token:
                # assign data and pop to parent node
                current_node.data = token
                current_node = stack.pop()

            # right paren - end an expr
            elif token == ')':
                # if stack not empty, pop to parent
                if not stack.is_empty():
                    current_node = stack.pop()
                else:
                    break
    

    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, aNode):
        # operators 
        if aNode.data in operators:
            if aNode.data == '+':
                return self.evaluate(aNode.lChild) + self.evaluate(aNode.rChild)
            elif aNode.data == '-':
                return self.evaluate(aNode.lChild) - self.evaluate(aNode.rChild) 
            elif aNode.data == '*':
                return self.evaluate(aNode.lChild) * self.evaluate(aNode.rChild)
            elif aNode.data == '/':
                return self.evaluate(aNode.lChild) / self.evaluate(aNode.rChild)
            elif aNode.data == '//':
                return self.evaluate(aNode.lChild) // self.evaluate(aNode.rChild)
            elif aNode.data == '%':
                return self.evaluate(aNode.lChild) % self.evaluate(aNode.rChild)
            elif aNode.data == '**':
                return self.evaluate(aNode.lChild) ** self.evaluate(aNode.rChild)

        # operands
        elif aNode.data.isdigit() or '.' in aNode.data:
            return float(eval(aNode.data))

    
    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode):
        # if node exists
        if (aNode != None):
            result = ""

            # if node has data, add data to result
            if aNode.data != None:
                result = str(aNode.data) + ' '
            # traverse children left to right
            result += self.pre_order(aNode.lChild)
            result += self.pre_order(aNode.rChild)

            return result
        return ""


    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode):
        # if node exists
        if (aNode != None):
            result = ""

            # traverse children left to right
            result += self.post_order(aNode.lChild)
            result += self.post_order(aNode.rChild)
            # if node has data, add data to result
            if aNode.data != None:
                result += str(aNode.data) + ' '

            return result 
        return ""


# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
 
    tree = Tree()
    tree.create_tree(expr)
    
    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()
