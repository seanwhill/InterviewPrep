#Basic string compression using counts of repeated characters. Only a-z if compressed is larger return original


'''
IDEAS:
1. Use a string builder?? python? this does not exist in python :(
2. O(N)
3. iterate through and 


abcdd

'''

from typing import *
import unittest
import time
from collections import defaultdict


def compress_string(s):
    compressed = []
    count = 0
    for i in range(len(s)):
        if i != 0 and s[i] != s[i - 1]:
            compressed.append(s[i - 1] + str(count))
            count = 0
        count += 1

    if count:
        compressed.append(s[-1] + str(count))
    
    return min(s, "".join(compressed), key = len)


class Test(unittest.TestCase):
    test_cases = [
        ("aabcccccaaa", "a2b1c5a3"),
        ("abcdef", "abcdef"),
        ("aabb", "aabb"),
        ("aaa", "a3"),
        ("a", "a"),
        ("", ""),
    ]
    testable_functions = [
        compress_string,
    ]

    def test_string_compression(self):
        for f in self.testable_functions:
            start = time.perf_counter()
            for _ in range(1000):
                for test_string, expected in self.test_cases:
                    assert f(test_string) == expected
            duration = time.perf_counter() - start
            print(f"{f.__name__} {duration * 1000:.1f}ms")


if __name__ == "__main__":
    unittest.main()



    