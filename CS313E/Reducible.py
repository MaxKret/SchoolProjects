#  File: Reducible.py

#  Description:

#  Student Name: Max Kretschmer

#  Student UT EID: mtk739

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 7/12/21

#  Date Last Modified: 7/16/21


import sys

# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime ( n ):
  if n==2 or n==3: 
    return True
  if n%2==0 or n<2: 
    return False
  for i in range(3, int(n**0.5)+1, 2):
    if n%i==0:
      return False    

  return True

# Input: takes as input a string in lower case and the size
#        of the hash table 
# Output: returns the index the string will hash into
def hash_word (s, size):
  hash_idx = 0
  for j in range (len(s)):
    hash_idx = (hash_idx * 26 + (ord (s[j]) - 96)) % size
  return hash_idx

# Input: takes as input a string in lower case and the constant
#        for double hashing 
# Output: returns the step size for that string 
def step_size (s, const):
  hash_idx = 0
  for j in range (len(s)):
    hash_idx = (hash_idx * 26 + (ord (s[j]) - 96)) % const
  return const - (hash_idx % const)

# Input: takes as input a string and a hash table 
# Output: no output; the function enters the string in the hash table, 
#         it resolves collisions by double hashing
def insert_word (s, hash_table):
  leng = len(hash_table)
  idx = hash_word(s, leng)

  #check if spot is occupied
  if (hash_table[idx] != ""):
    stepSize = step_size(s, 13)
    #use step size to check for spots
    i = 1
    while (hash_table[(idx + stepSize * i) % leng] != ""):
      i += 1
    hash_table[(idx + stepSize * i) % leng] = s

  #if not occupied, place word
  else:
    hash_table[idx] = s

# Input: takes as input a string and a hash table 
# Output: returns True if the string is in the hash table 
#         and False otherwise
def find_word (s, hash_table):
  leng = len(hash_table)
  idx = hash_word(s, leng)
  
  if (hash_table[idx] == s):
    return True
  
  if (hash_table[idx] != ""):
    stepSize = step_size(s, 7)
    i = 1
    while (hash_table[(idx + stepSize * i) % leng] != ""):
      if (hash_table[(idx + stepSize * i) % leng] == s):
        return True
      i += 1
  return False

# Input: string s, a hash table, and a hash_memo 
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo 
#         and returns True and False otherwise
def is_reducible (s, hash_table, hash_memo):
  if find_word(s, hash_memo):
    return True

  #check if fully reduced to one letter
  if len(s) == 1:
    return s in ["a", "i", "o"]

  #recursive loop for checking if fully reducible
  for reducedWord in reducible_helper(s, hash_table):
    if is_reducible(reducedWord, hash_table, hash_memo):
      insert_word(s, hash_memo)
      return True

  return False

# Input: string s, a hash table; checks a word to find reductions
# Output: if the string is reducible it returns all slices of the word
def reducible_helper(s, hash_table):
  reducible_word_list = []  

  #subtract a letter from each word and test each slice
  for i in range(len(s)):
    slice = s[:i] + s[i+1:]
    if find_word(slice, hash_table):
      reducible_word_list.append(slice)
  return reducible_word_list

# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words (string_list):
  longest_words =[]
  largest_size = 0
  for idx in range(len(string_list)):

    #SIZE == LARGEST SIZE
    if len(string_list[idx]) == largest_size:
      longest_words.append(string_list[idx])

    #SIZE > LARGEST SIZE
    if len(string_list[idx]) > largest_size:
      largest_size = len(string_list[idx])
      longest_words = []
      longest_words.append(string_list[idx])

  return longest_words



def main():
  # create an empty word_list
  word_list = []
  #append single letter words
  word_list.extend(["a", "i", "o"])
  # read words from words.txt and append to word_list
  for line in sys.stdin:
      line = line.strip()
      word_list.append (line)

  # find length of word_list
  # determine prime number N that is greater than twice
  # the length of the word_list
  N = len(word_list)*2
  while (not is_prime(N)):
    N += 1

  # create an empty hash_list
  hash_list = []
  # populate the hash_list with N blank strings
  for i in range(N):
    hash_list.append("")
  # hash each word in word_list into hash_list
  # for collisions use double hashing 
  for word in word_list:
    insert_word(word, hash_list)

  # create an empty hash_memo of size M
  hash_memo = []
  # we do not know a priori how many words will be reducible
  # let us assume it is 10 percent (fairly safe) of the words
  # then M is a prime number that is slightly greater than 
  # 0.2 * size of word_list
  M = int(len(word_list)*0.20)
  while (not is_prime(M)):
    M += 1
  # populate the hash_memo with M blank strings
  for i in range(M):
    hash_memo.append("")
  # create an empty list reducible_words
  reducible_words = []
  # for each word in the word_list recursively determine
  # if it is reducible, if it is, add it to reducible_words
  # as you recursively remove one letter at a time check
  # first if the sub-word exists in the hash_memo. if it does
  # then the word is reducible and you do not have to test
  # any further. add the word to the hash_memo.
  for s in word_list:
    _reducible = is_reducible(s, hash_list, hash_memo)
    if _reducible:
      reducible_words.append(s)

  # find the largest reducible words in reducible_words
  largest_reducible_words = get_longest_words(reducible_words)
  largest_reducible_words = sorted(largest_reducible_words)

  # print the reducible words in alphabetical order
  # one word per line
  for word in largest_reducible_words:
    print(word)

if __name__ == "__main__":
  main()