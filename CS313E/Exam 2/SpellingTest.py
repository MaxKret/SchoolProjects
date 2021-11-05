#  File: SpellingTest.py

#  Description: Determine whether a given string can be spelled using a combination of smaller strings.

#  Student Name: Maxwell Kretschmer

#  Student UT EID: mtk739

#  Course Name: CS 313E

#  Unique Number: 86610

import sys


def permuter (lst, idx, s, bool):
    '''
    recursively finds all permutations of lst
    returns True if a correct arrangement is found
    '''
    hi = len(lst)
    if (idx == hi):
        if s in "".join(lst):
            bool = True
            return bool
        return bool

    else:
        for i in range (idx, hi):
            lst[idx], lst[i] = lst[i], lst[idx]
            if permuter(lst, idx + 1, s, bool):
                return True
            lst[idx], lst[i] = lst[i], lst[idx]
        return bool



def spelling_test(s, l):
    # FILL THIS IN: determine whether the string s can be formed by combining strings in the list l
    return permuter(l, 0, s, False)


def main():
    s = input()
    lines = sys.stdin.readlines()

    print(spelling_test(s, [line.replace('\n', '') for line in lines]))

if __name__ == "__main__":
    main()