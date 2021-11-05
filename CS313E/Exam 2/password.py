#  File: password.py

#  Description: Rotates a linked list to the left (counter-clockwise) ``r_step'' steps ``times'' times 

#  Student Name: Maxwell Kretschmer

#  Student UT EID: mtk739

#  Course Name: CS 313E

#  Unique Number: 86610

import sys

class Link (object):
    # do not change this constructor
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next

class LinkedList (object):
    # create a linked list -- do not change this constructor
    def __init__(self):
        self.first = None

    # helper function to add an item at the end of a list
    # you can use this if you want, but do not delete it
    def insert_last (self, data): 
        newLink = Link(data)
        current = self.first

        if current == None:
            self.first = newLink
            return

        while current.next != None:
            current = current.next

        current.next = newLink

    # helper function to add an item at the start of a list
    # you can use this if you want, but do not delete it
    def insert_first (self, data): 
        newLink = Link(data)

        newLink.next = self.first
        self.first = newLink


    # helper function to copy the contents of the current linked list
    # returns new linked list
    # you can use this if you want, but do not delete it
    def copy_list(self):
        new_list = LinkedList()
        curr = self.first
        while curr:
            new_list.insert_last(curr.data)
            curr = curr.next
        return new_list

    # helper function to count number of links
    # returns number of links
    # you can use this if you want, but do not delete it
    def num_links(self):
        curr = self.first
        res = 0
        while curr:
            res += 1
            curr = curr.next
        return res

    # string representation of data 10 items to a line, 2 spaces between data
    def __str__ (self):
        curr_items = []
        curr = self.first
        res = ""
        while curr:
            curr_items.append(curr.data)
            if len(curr_items) == 10:
                res += "  ".join(map(str, curr_items)) + "\n"
                curr_items = []
            curr = curr.next
        # print the remaining items
        if len(curr_items):
            res += "  ".join(map(str, curr_items))
        return res


    # COMPLETE THIS FUNCTION
    def rotateOnce(self, r_step):
        # select first node
        current = self.first

        # traverse list until end
        while (current.next != None):
            current = current.next

        current.next = self.first
        current = self.first
        
        for i in range(r_step - 1):
            current = current.next

        # Update the self.first pointer and set current's next to None
        self.first = current.next
        current.next = None

        return self


    # return a new linked list that results from the rotation
    # do not change this linked list
    def rotate(self, r_step, times):
        ll_copy = self.copy_list()
        if r_step == 0:
            return ll_copy

        while times > 0:
            ll_copy = ll_copy.rotateOnce(r_step)
            times -= 1
        
        return ll_copy

    

        
        
# DO NOT CHANGE MAIN
def main():
    ll = LinkedList()
    
    data = list(map(int, input().split()))

    # populate linked list with data
    for d in data:
        ll.insert_last(d)

    r_step, times = list(map(int, input().split()))

    rotated = ll.rotate(r_step, times)
    # print the original list
    print(ll)
    # print the new list that results from calling rotate()
    print(rotated)

if __name__ == "__main__":
    main()