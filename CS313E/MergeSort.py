def Merge(numbers, i, j, k) :
    mergedSize = k - i + 1                # Size of merged partition
    mergePos = 0                          # Position to insert merged number
    leftPos = 0                           # Position of elements in left partition
    rightPos = 0                          # Position of elements in right partition
    mergedNumbers = [0 for x in range(mergedSize)]   # Dynamically allocates temporary array for merged numbers
    leftPos = i                           # Initialize left partition position
    rightPos = j + 1                      # Initialize right partition position
   
   # Add smallest element from left or right partition to merged numbers
    while (leftPos <= j and rightPos <= k) :
        if (numbers[leftPos] <= numbers[rightPos]) :
            mergedNumbers[mergePos] = numbers[leftPos]
            leftPos += 1
      
        else :
            mergedNumbers[mergePos] = numbers[rightPos]
            rightPos += 1 
         
      
        mergePos += 1 
   
   
   # If left partition is not empty, add remaining elements to merged numbers
    while (leftPos <= j) :
        mergedNumbers[mergePos] = numbers[leftPos]
        leftPos += 1 
        mergePos += 1 
   
   
   # If right partition is not empty, add remaining elements to merged numbers
    while (rightPos <= k) :
        mergedNumbers[mergePos] = numbers[rightPos]
        rightPos += 1 
        mergePos += 1 
    print()
   
   # Copy merge number back to numbers
    for mergePos in range(mergedSize):
        numbers[i + mergePos] = mergedNumbers[mergePos]


def MergeSort(numbers, i, k) :
    j = 0
    if (i < k) :
        j = int((i + k) / 2 ) # Find the midpoint in the partition
      
      # Recursively sort left and right partitions
        MergeSort(numbers, i, j)
        MergeSort(numbers, j + 1, k)
      
      # Merge left and right partition in sorted order
        Merge(numbers, i, j, k)
   


def main() :
    numbers = [25,92,58,89,82]
   
    print("UNSORTED: ")
    print(numbers)
    
    print()
    
    MergeSort(numbers, 0, len(numbers) - 1)
    
    print("SORTED: ")
    print(numbers)
    
    print()

if __name__ == '__main__':
    main()