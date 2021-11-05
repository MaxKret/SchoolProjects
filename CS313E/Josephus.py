#  File: Josephus.py

#  Description: We use a circular linked list to represent a circle of soldiers, eliminating one at a time in a specifed interval.

#  Student Name: Maxwell Kretschmer

#  Student UT EID: mtk739

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 7/26/21

#  Date Last Modified: 7/30/21

import sys
class Link (object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next

class CircularList(object):
    # Constructor
    def __init__ ( self ): 
        self.first = None

    # Insert an element (value) in the list
    def insert ( self, data ):
        if data != None:
            newLink = Link(data)
            if self.first == None:
                self.first = newLink
                self.first.next = self.first
            else:
                current = self.first
                while(current.next != self.first):
                    current = current.next
                current.next = newLink
                current = current.next
                current.next = self.first

    # Find the Link with the given data (value)
    # or return None if the data is not there
    def find ( self, data ):
        current = self.first
        # If list is empty
        if current == None:
            return None
        # non-empty list
        else:
            while (current.data != None) and (current.data != data):
                current = current.next
                if current == self.first: # if list fully traversed
                    break
            # Check if data not found
            if current.data != data:
                return None
            return current


    # Delete a Link with a given data (value) and return the Link
    # or return None if the data is not there
    def delete ( self, data ):
    # setup
        # check if list is empty
        if self.first == None:
            return None
        # check if data is in list
        if self.find(data) == None:
            return None
        
        current = self.first
        previous = self.first

        # circle the list to put previous into place
        while previous.next != self.first:
            previous = previous.next

    # algorithm
        # find link that has the data given
        while (current.data != data):
            previous = current
            current = current.next

        # link found
        if (self.first != self.first.next):
            # connect the previous link to the next link
            previous.next = current.next
            # if the deleted link was the first node, then re-set the first node
            if current == self.first:
                self.first = current.next
		# if self.first == self.first.next, then list only has 1 element
        else:
            self.first = None

		


    # Delete the nth Link starting from the Link start 
    # Return the data of the deleted Link AND return the
    # next Link after the deleted Link in that order
    def delete_after ( self, start, n ):
        # check if list is empty
        if self.first == None:
            return None, None

        # find data in list
        current = self.find(start.data)

        # check if list is empty
        if current == None:
            return None, None

        # step forward in the list elim_num steps
        for i in range (1, n):
            current = current.next

        # set up return data before altering list
        data = current.data
        nextLink = current.next
		
        # delete link
        self.delete(current.data)

        return data,nextLink
        

    # Return a string representation of a Circular List
    # The format of the string will be the same as the __str__ 
    # format for normal Python lists
    def __str__ ( self ):
        result = []
        current = self.first
        # empty list
        if current == None or current.data == None:
            return "[]"

		# traverse until we reach the starting link
        while (current.next != self.first):
            result.append(current.data)
            current = current.next

		# when current.next == self.first, return the string
        result.append(current.data)
        return str(result)

def main():
    # read number of soldiers
    line = sys.stdin.readline()
    line = line.strip()
    num_soldiers = int (line)
    
    # read the starting number
    line = sys.stdin.readline()
    line = line.strip()
    start_count = int (line)

    # read the elimination number
    line = sys.stdin.readline()
    line = line.strip()
    elim_num = int (line)

    # initialize list
    soldiers = CircularList()

    for i in range (1, num_soldiers + 1):
        soldiers.insert(i) 

    #print(soldiers)

    # loop setup
    start = soldiers.first # "1"
    for i in range(start_count-1): # for st_ct = 3, (st_ct-1):2  i:0,1
        start = start.next


    _hasSoldiers = True
    # loop through list while it still has soldiers
    if soldiers.first != None:
        while _hasSoldiers:
            data,start = soldiers.delete_after(start, elim_num)
            if data == None:
                _hasSoldiers = False
            else:
                print(str(data))
    

if __name__ == "__main__":
  main()