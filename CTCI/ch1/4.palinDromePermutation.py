# Given a string write a function to check if it's a premutation of a palindrome. The palindrome does not need to be 
# limited to just dictionary words, you can ignore casing and non letter chars

# Ex 
'''
A palindrome is the same back as it is forward. So a permutation of a palindrome will have 
an even number of letters unless it's the center most letter

Questions:
Does case matter?

Ideas:

1. Array of 128 for each letter char then give ONE opportunity for there to be an extra char
2. Same idea but with a hashmap keeping track of letters

Examples

Tact Coa
...2ts 2a 2cs

'''


from typing import *
import unittest
import time
from collections import defaultdict


# gets the distance from A so that it can fit in the range 0 - 25
def char_number(c):
    a = ord("a")
    z = ord("z")

    a_u = ord("A")
    z_u = ord("Z")

    val = ord(c)

    if a <= val <= z :
        return val - a

    if(a_u <= val <= z_u):
        return val - a_u

    return - 1


def is_palindrome_permutation(s):
    table = [0 for _ in range(ord("z") - ord("a") + 1)]
    # table = [0] * (ord("z") - ord("a") + 1)

    countOdd = 0
    #build table
    for c in s:
        val = char_number(c)
        if val != -1:
            table[val] += 1
            if(table[val] % 2 == 1):
                countOdd += 1
            else:
                countOdd -= 1

    return countOdd <= 1

def is_palindrome_permutation_2(s):
    table = [0] * (ord("z") - ord("a") + 1)

    #build table
    for c in s:
        val = char_number(c)
        if val != -1:
            table[val] += 1

    foundOdd = False

    for count in table:
        if count % 2 == 1:
            if(foundOdd):
                return False
            else:
                foundOdd = True
    return True


def is_palindrome_permutation_pythonic(phrase):
    """function checks if a string is a permutation of a palindrome or not"""
    counter = Counter(phrase.replace(" ", "").lower())
    return sum(val % 2 for val in counter.values()) <= 1


class Test(unittest.TestCase):
    test_cases = [
        ("aba", True),
        ("aab", True),
        ("abba", True),
        ("aabb", True),
        ("a-bba", True),
        ("Tact Coa", True),
        ("jhsabckuj ahjsbckj", True),
        ("Able was I ere I saw Elba", True),
        ("So patient a nurse to nurse a patient so", False),
        ("Random Words", False),
        ("Not a Palindrome", False),
        ("no x in nixon", True),
        ("azAZ", True),
    ]
    testable_functions = [is_palindrome_permutation, is_palindrome_permutation_2, is_palindrome_permutation_pythonic]

    def test_pal_perm(self):
        for f in self.testable_functions:
            print("running " + f.__name__)
            for [test_string, expected] in self.test_cases:
                assert f(test_string) == expected


if __name__ == "__main__":
    unittest.main()