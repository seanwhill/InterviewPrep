#Write a method to replace all spaces in a string with %20. You may assume that the string has sufficient space at the end to 
#hold the additional characters, and that you are given the "true" length of the string. supposed to use char array in beginning

#EX
# INPUT "HELLO FRIEND  ", 12
# OUTPUT "HELLO%20FRIEND"

'''
IDEAS:

Is the extra length in the string just enough for the %20s? or do you need more

1. should be O(N)
2 (bad). Could just replace  " " with %20 easily only if there aren't 'real' trailing spaces. defeats the problem though. That also creates another string so that's no good
3. start from back and use the offset from the 'real' length and the length of the entire string including the additional spaces 

'''

#chars = list(s) is how you could split it if you wanted

from typing import *
import unittest
import time
from collections import defaultdict

def urlify(str, trueLength):
    chars = list(str)
    oldIndex = trueLength - 1
    newindex = len(chars) - 1

    while oldIndex >= 0:
        if(chars[oldIndex] == " "):
            chars[newindex] = "0"
            chars[newindex - 1] ="2"
            chars[newindex -2] = "%"
            newindex -= 3
        else:
            chars[newindex] = chars[oldIndex]
            newindex -= 1
        oldIndex -= 1

    return "".join(chars)

def urlify_pythonic(str, trueLength):
    return str[:trueLength].replace(" ", "%20")


#INITIAL IDEA THAT WOULDN'T WORK BECAUSE eventually you catch up to the old string
# def urlify(chars, trueLength):
#     offset = len(chars) - trueLength

#     for i in range(len(chars) - 1, -1):
#         i - offset

#         if(chars[i-offset] == " "):
#             chars[i] = "0"
#             chars[i - 1] ="2"
#             chars[i - 3] = "%"
#         else:
#             chars[i] = chars[i - offset]

class Test(unittest.TestCase):
    """Test Cases"""

    test_cases = {
        ("much ado about nothing      ", 22): "much%20ado%20about%20nothing",
        ("Mr John Smith    ", 13): "Mr%20John%20Smith",
        (" a b    ", 4): "%20a%20b",
        (" a b       ", 5): "%20a%20b%20",
    }
    testable_functions = [urlify, urlify_pythonic]

    def test_urlify(self):
        for urlify in self.testable_functions:
            for args, expected in self.test_cases.items():
                actual = urlify(*args)
                assert actual == expected, f"Failed {urlify.__name__} for: {[*args]}"




if __name__ == "__main__":
    unittest.main()