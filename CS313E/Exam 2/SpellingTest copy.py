#  File: SpellingTest.py

#  Description: Determine whether a given string can be spelled using a combination of smaller strings.

#  Student Name: Maxwell Kretschmer

#  Student UT EID: mtk739

#  Course Name: CS 313E

#  Unique Number: 86610

import sys


def permuter (l, idx, permutations):
    '''
    recursively finds all permutations of strings in l
    returns all permutations of l, storing them in permutations
    '''
    hi = len(l)
    if (idx == hi):
        permutations.append(l[:])
        return permutations
    else:
        for i in range (idx, hi):
            l[idx], l[i] = l[i], l[idx]
            permuter(l, idx + 1, permutations)
            l[idx], l[i] = l[i], l[idx]
        return permutations


def sum_of_strings(s, Lst):
    '''
    concat's a list of strings into one string
    '''
    result = ""
    for strng in Lst:
        result += strng
        if result == s:
            return result
    return result


def spelling_test(s, l):
    # FILL THIS IN: determine whether the string s can be formed by combining strings in the list l
    permutations = []
    permutations = permuter(l, 0, permutations)
    _does_eq_l = False

    for perm in permutations:
        if sum_of_strings(s, perm) == s:
            _does_eq_l = True
            break

    return _does_eq_l


def main():
    s = input()
    lines = sys.stdin.readlines()

    print(spelling_test(s, [line.replace('\n', '') for line in lines]))

if __name__ == "__main__":
    main()