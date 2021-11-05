def Partition(numbers, lowIndex, highIndex) :
   # Pick middle element as pivot
   midpoint = lowIndex + (int((highIndex - lowIndex) / 2))
   pivot = numbers[midpoint]
   
   done = False
   while (not done) :
      # Increment lowIndex while numbers[lowIndex] < pivot
      while (numbers[lowIndex] < pivot) :
         lowIndex += 1
      
      
      # Decrement highIndex while pivot < numbers[highIndex]
      while (pivot < numbers[highIndex]) :
         highIndex -= 1
      
      
      # If zero or one elements remain, then all numbers are 
      # partitioned. Return highIndex.
      if (lowIndex >= highIndex) :
         done = True
      
      else :
         # Swap numbers[lowIndex] and numbers[highIndex]
         temp = numbers[lowIndex]
         numbers[lowIndex] = numbers[highIndex]
         numbers[highIndex] = temp
         
         # Update lowIndex and highIndex
         lowIndex += 1
         highIndex -= 1
      
   
   
   return highIndex


def Quicksort(numbers, lowIndex, highIndex) :
   # Base case: If the partition size is 1 or zero 
   # elements, then the partition is already sorted
   if (lowIndex >= highIndex) :
      return
   
   
   # Partition the data within the array. Value lowEndIndex 
   # returned from partitioning is the index of the low 
   # partition's last element.
   lowEndIndex = Partition(numbers, lowIndex, highIndex)
   
   # Recursively sort low partition (lowIndex to lowEndIndex) 
   # and high partition (lowEndIndex + 1 to highIndex)
   Quicksort(numbers, lowIndex, lowEndIndex)
   Quicksort(numbers, lowEndIndex + 1, highIndex)


def main():
   numbers = [15, 29, 53, 32, 10, 62, 60, 93]
  
   print("UNSORTED: ", end="")
   print(numbers)
   
   
   # Initial call to quicksort
   Quicksort(numbers, 0, 4)
   
   print("SORTED: ", end="")
   print(numbers)
   

if __name__ == "__main__":
  main()
