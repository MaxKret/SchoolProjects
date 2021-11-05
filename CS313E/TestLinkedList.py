#  File: TestLinkedList.py

#  Description:

#  Student Name: Maxwell Kretschmer

#  Student UT EID: mtk739

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 7/21/21

#  Date Last Modified: 7/26/21

import sys
class Link (object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next

class LinkedList (object):
    # create a linked list
    # you may add other attributes
    def __init__ (self):
        self.first = None

    # get number of links 
    def get_num_links (self):
        i = 0
        currentLink = self.first
        while currentLink != None:
            i += 1
            currentLink = currentLink.next
        return i


    # add an item at the beginning of the list
    def insert_first (self, data):
        newLink = Link (data)
        newLink.next = self.first
        self.first = newLink


    def insert_last (self, data):
        newLink = Link (data)
        currentLink = self.first

        if (currentLink == None):
            self.first = newLink
            return

        while (currentLink.next != None):
            currentLink = currentLink.next

        currentLink.next = newLink


    # add an item in an ordered list in ascending order
    # assume that the list is already sorted
    def insert_in_order (self, data): 
        if self.first == None:
            self.insert_first(data)
            return
        if data < self.first.data:
            self.insert_first(data)
            return
        else:
            newLink = Link(data)
            currentLink = self.first
            previousLink = self.first
            while (data > currentLink.data):
                if currentLink.next == None:
                    self.insert_last(data)
                    return
                else:
                    previousLink = currentLink
                    currentLink = currentLink.next
            previousLink.next = newLink
            newLink.next = currentLink


    # search in an unordered list, return None if not found
    def find_unordered (self, data): 
        currentLink = self.first
        if currentLink == None:
            return None
        else:
            while (currentLink.data != data):
                if currentLink.next == None:
                    return None
                else:
                    currentLink = currentLink.next
            return currentLink


    # Search in an ordered list, return None if not found
    def find_ordered (self, data): 
        currentLink = self.first
        if currentLink == None:
            return None
        else:
            while (currentLink.data != data):
                if currentLink.next == None:
                    return None
                else:
                    if currentLink.next.data > data:
                        return None 
                    else:
                        currentLink = currentLink.next
            return currentLink


    # Delete and return the first occurrence of a Link containing data
    # from an unordered list or None if not found
    def delete_link (self, data):
        currentLink = self.first
        previousLink = self.first

        if (currentLink == None):
            return None

        while (currentLink.data != data):
            if (currentLink.next == None):
                return None
            else:
                previousLink = currentLink
                currentLink = currentLink.next

        if (currentLink == self.first):
            self.first = self.first.next
        else:
            previousLink.next = currentLink.next

        return currentLink


    # String representation of data 10 items to a line, 2 spaces between data
    def __str__ (self):
        currentLink = self.first
        i = 0
        result = ''    
        if self.is_empty():
            return ""
        
        for i in range(self.get_num_links() - 1):
            result += str(currentLink.data) + '  '
            currentLink = currentLink.next
            i += 1
        
        result += str(currentLink.data)

        result_nums = result.split("  ")
        final_result = ""
        i = 0
        for num in result_nums:
            i += 1
            if i < 10:
                final_result += str(num) + "  "
            else:
                final_result += str(num) + "\n"

            if i == 10:
                i = 0

        return final_result


    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted (self):
        currentLink = self.first
        if self.is_empty() or self.get_num_links() == 1:
            return True
        
        for i in range(self.get_num_links() - 1):
            if currentLink.data > currentLink.next.data:
                return False
            currentLink = currentLink.next
        return True


    # Return True if a list is empty or False otherwise
    def is_empty (self): 
        return (self.first == None)


    # Copy the contents of a list and return new list
    # do not change the original list
    def copy_list (self):
        result_list = LinkedList()
        currentLink = self.first
        while (currentLink != None):
            result_list.insert_last(currentLink.data)
            currentLink = currentLink.next
        return result_list
        

    # Reverse the contents of a list and return new list
    # do not change the original list
    def reverse_list (self):
        result_list = LinkedList()
        currentLink = self.first
        while (currentLink != None):       
            result_list.insert_first(currentLink.data)
            currentLink = currentLink.next
        return result_list


    # Sort the contents of a list in ascending order and return new list
    # do not change the original list
    def sort_list (self): 
        result_list = LinkedList()
        if self.is_empty():
            return result_list

        currentLink = self.first
        for i in range(self.get_num_links()):
            result_list.insert_in_order(currentLink.data)
            currentLink = currentLink.next  
        
        return result_list



    # Merge two sorted lists and return new list in ascending order
    # do not change the original lists
    def merge_list (self, other): 
        currentLink = other.first
        result = self.copy_list().sort_list()

        if self.is_empty():
            if other.is_empty():
                return result
            else:
                result = other.copy_list()
                return result

        elif other.is_empty():
            return result

        for i in range(other.get_num_links()):
            result.insert_in_order(currentLink.data)
            currentLink = currentLink.next

        return result


    # Test if two lists are equal, item by item and return True
    def is_equal (self, other):
        if self.get_num_links() != other.get_num_links():
            return False
        
        if self.is_empty() and other.is_empty():
            return True
        
        currentLinka = self.first
        currentLinkb = other.first
        
        for i in range(self.get_num_links()):
            if currentLinka.data != currentLinkb.data:
                return False
            currentLinka = currentLinka.next
            currentLinkb = currentLinkb.next
        
        return True


    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    # do not change the original list
    def remove_duplicates (self):
        result = self.copy_list()
        previousLink = result.first
        currentLink = result.first
        links = []

        for i in range(result.get_num_links()):
            if currentLink.data in links:
                currentLink = currentLink.next
                previousLink.next = currentLink
            else:
                links.append(currentLink.data)
                previousLink = currentLink
                currentLink = currentLink.next
            
        return result


def main():
    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    ll1 = LinkedList()

    for i in range (1, 11):
        ll1.insert_first(i)

    print(ll1, "\n")


    # Test method insert_last()
    ll1.insert_last(11)
    print(ll1,"\n")


    # Test method insert_in_order()
    ll2 = LinkedList()
    x = [1, 4, 5, 6]
    for i in x:
        ll2.insert_last(i)

    ll2.insert_in_order(3)
    print(ll2, "\n")


    # Test method get_num_links()
    print(ll2.get_num_links(), "\n")


    # Test method find_unordered() 
    # Consider two cases - data is there, data is not there 
    ll3 = LinkedList()
    x = [1, 4, 5, 2]
    for i in x:
        ll3.insert_first(i)
    print(ll3.find_unordered(3), "\n") #not there
    print(ll3.find_unordered(1), "\n") #there


    # Test method find_ordered() 
    # Consider two cases - data is there, data is not there 
    print(ll2.find_ordered(2), "\n") #not there
    print(ll2.find_ordered(4), "\n") #there


    # Test method delete_link()
    # Consider two cases - data is there, data is not there
    print(ll2.delete_link(2), "\n") #not there
    print(ll2.delete_link(4), "\n") #there


    # Test method copy_list()
    ll4 = LinkedList()
    x = [1, 4, 5, 2, 3]
    for i in x:
        ll4.insert_first(i)
        
    print("original list:",ll4, "\n")
    ll4b = ll4.copy_list()
    print("copied list:", ll4b, "\n")


    # Test method reverse_list()
    print("original list:",ll4, "\n")
    ll4b = ll4.reverse_list()
    print("reversed list:", ll4b, "\n")


    # Test method sort_list()
    print("original list:",ll4, "\n")
    ll4b = ll4.sort_list()
    print("sorted list:", ll4b, "\n")


    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted
    print("original list is sorted:",ll4.is_sorted(), "\n")
    ll4b = ll4.sort_list()
    print("sorted list is sorted:", ll4b.is_sorted(), "\n")

    # Test method is_empty()
    ll5 = LinkedList()
    print("Empty List is empty:",ll5.is_empty(), "\n")
    print("Non-empty List is empty:", ll4.is_empty(), "\n")

    # Test method merge_list()
    lla = LinkedList()
    llb = LinkedList()
    x = [1, 2, 5]
    y = [3, 4, 6]
    for i in x:
        lla.insert_last(i)
    for i in y:
        llb.insert_last(i)


    print("List 1:",lla, "\n")
    print("List 2:", llb, "\n")
    llmerged = lla.merge_list(llb)
    print("Merged List:", llmerged, "\n")


    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal
    print(ll4,"is equal to",ll3,":", ll4.is_equal(ll3), "\n")
    ll4b = ll4.copy_list()
    print(ll4,"is equal to",ll4b,":", ll4.is_equal(ll4b), "\n")

    # Test remove_duplicates()
    ll6 = LinkedList()
    x = [1, 2, 1, 3, 1, 2, 5, 5]
    for i in x:
        ll6.insert_last(i)
    
    print("original list:",ll6, "\n")
    ll6b = ll6.remove_duplicates()
    print("duplicates removed:", ll6b, "\n")


if __name__ == "__main__":
  main()