import sys


def insertion_sort1 (a):
  for i in range (1, len(a)):
    j = i
    while ((j > 0) and (a[j] < a[j - 1])):
      a[j], a[j - 1] = a[j - 1], a[j]
      j += -1

def insertion_sort2 (a):
  for i in range (1, len(a)):
    tmp = a[i]
    j = i
    while ((j > 0) and (a[j - 1] > tmp)):
      a[j] = a[j - 1]
      j += -1
    a[j] = tmp
    


# Python program for implementation of Shell Sort
  
def shellSort(arr, gaps):
  
    # Start with a big gap, then reduce the gap
    n = len(arr)
    idx = 0
    gap = gaps[idx]
  
    # Do a gapped insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already in gapped 
    # order keep adding one more element until the entire array
    # is gap sorted
    while gap > 0:
  
        for i in range(gap,n):
  
            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = arr[i]
  
            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            while  j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j -= gap
  
            # put temp (the original a[i]) in its correct location
            arr[j] = temp
        idx += 1
        gap = gaps[idx]

def qsort1 (a, lo, hi):
  if (lo >= hi):
    return

  pivot = a[lo]
  m = lo
  for i in range (lo, hi + 1):
    if (a[i] < pivot):
      m = m + 1
      a[m], a[i] = a[i], a[m]
  
  a[lo], a[m] = a[m], a[lo]

  qsort1 (a, lo, m - 1)
  qsort1 (a, m + 1, hi)

def qsort2 (a, lo, hi):
  if (lo >= hi):
    return

  left = lo
  right = hi
  pivot = a[(lo + hi) // 2]

  while (left < right):
    while (a[left] < pivot):
      left = left + 1
    while (pivot < a[right]):
      right = right - 1

    if (left <= right):
      a[left], a[right] = a[right], a[left]
      left = left + 1
      right = right - 1

  qsort2 (a, lo, right)
  qsort2 (a, left, hi)





def main():
    a = [44, 83, 30, 64, 86, 97, 80]
    qsort1(a,0,6)
    qsort2(a,0,6)

if __name__ == "__main__":
  main()
