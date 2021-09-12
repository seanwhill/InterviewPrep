#Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures.

from typing import *
import unittest
import time
from collections import defaultdict

'''
Ideas:
1. Iterate through each and check if in map
2.  Iterate through and check if in Array where index is ASCII value
    What is the set of characters? Assume ASCII 128

3.one line with using set python



'''
#O(N)
def is_unique (s: str):
    chars = [False] * 128
    for c in s:
        val = ord(c)
        if chars[val]:
            return False
        chars[val] = True
    
    return True


#O(1) ????
def is_unique_one_line(s):
    return len(set(s)) == len(s)

def is_unique_dict(s):
    dict = {}
    for c in s:
        if c in dict:
            return False
        dict[c] = 1
    return True

    
class Test(unittest.TestCase):
    test_cases = [
        ("abcd", True),
        ("s4fad", True),
        ("", True),
        ("23ds2", False),
        ("hb 627jh=j ()", False),
        ("".join([chr(val) for val in range(128)]), True),  # unique 128 chars
        ("".join([chr(val // 2) for val in range(129)]), False),  # non-unique 129 chars
    ]
    test_functions = [
        is_unique,
        is_unique_one_line,
        is_unique_dict
    ]

    def test_is_unique_chars(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)

        for _ in range(num_runs):
            for text, expected in self.test_cases:
                for is_unique_chars in self.test_functions:
                    start = time.perf_counter()
                    assert (
                        is_unique_chars(text) == expected
                    ), f"{is_unique_chars.__name__} failed for value: {text}"
                    function_runtimes[is_unique_chars.__name__] += (
                        time.perf_counter() - start
                    ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name}: {runtime:.1f}ms")


if __name__ == "__main__":
    unittest.main()

