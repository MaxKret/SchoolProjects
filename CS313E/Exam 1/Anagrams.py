# File: Anagrams.py

# Description: A program to group strings into anagram families

# Student Name: Maxwell Kretschmer

# Student UT EID: mtk739

# Course Name: CS 313E

# Unique Number: 86610


# Input: lst is a list of strings comprised of lowercase letters only
# Output: the number of anagram families formed by lst
def anagram_families(lst):
    #SETUP
    sorted_list = []
    setList = set()
    
    #SORT
    for word in lst:
        sorted_list.append("".join(sorted(word)))

    setList = set(sorted_list)
    return len(setList)

def main():
    # read the number of strings in the list, add the input strings into a list
    import sys
    inLines_unformatted = sys.stdin.readlines()
    inLines = [entry.strip("\n").strip() for entry in inLines_unformatted]
    numLines = int(inLines[0])
    del inLines[0]

    # compute the number of anagram families
    num_families = anagram_families(inLines)
    # print the number of anagram families
    sys.stdout.write("{}".format(num_families))

if __name__ == "__main__":
    main()