#There are three types of edits that can be performed on stringsL insert, remove, or replace.
#Given two strings write a function to check if they are one away or zero edits


'''
Ideas: 

probably O(n)

1. insert and remove are probably same things
2. replace would be different character 
3. when reach a value different you can check if it's an insert or removal from the next chars
pale, ple ... reach a is different then l so you check now l and l are the same so that would be a remove
pale, plle ... same thing but since they are same length you'd know that was the switch there and keep going
'''

from typing import *
import unittest
import time
from collections import defaultdict

def is_one_away(s1, s2):
    len1 = len(s1)
    len2 = len(s2)

    if(len1 == len2):
        return checkReplacement(s1, s2)
    elif len1 == len2 + 1:
        return checkInsertDelete(s1, s2)
    elif len1 + 1  == len2:
        return checkInsertDelete(s2, s1)
    return False
def checkReplacement(s1, s2): #Can add len variable but I chose not to just gonna recalc
    numReplace = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if(numReplace == 1):
                return False
            numReplace += 1
    return True

#s1 is larger than s2
def checkInsertDelete(s1, s2):
    i, j = 0, 0 
    edited = False
    while j < len(s2) and i < len(s1):
        if s1[i] != s2[j]:
            if edited:
                return False
            edited = True
            i += 1
        else:
            i += 1
            j += 1

    return True


class Test(unittest.TestCase):
    test_cases = [
        # no changes
        ("pale", "pale", True),
        ("", "", True),
        # one insert
        ("pale", "ple", True),
        ("ple", "pale", True),
        ("pales", "pale", True),
        ("ples", "pales", True),
        ("pale", "pkle", True),
        ("paleabc", "pleabc", True),
        ("", "d", True),
        ("d", "de", True),
        # one replace
        ("pale", "bale", True),
        ("a", "b", True),
        ("pale", "ble", False),
        # multiple replace
        ("pale", "bake", False),
        # insert and replace
        ("pale", "pse", False),
        ("pale", "pas", False),
        ("pas", "pale", False),
        ("pkle", "pable", False),
        ("pal", "palks", False),
        ("palks", "pal", False),
        # permutation with insert shouldn't match
        ("ale", "elas", False),
    ]   

    testable_functions = [is_one_away]

    def test_one_away(self):

        for f in self.testable_functions:
            start = time.perf_counter()
            for _ in range(100):
                for [text_a, text_b, expected] in self.test_cases:
                    assert f(text_a, text_b) == expected
            duration = time.perf_counter() - start
            print(f"{f.__name__} {duration * 1000:.1f}ms")


if __name__ == "__main__":
    unittest.main()