# Given two strings, write a method to decide if one is a permutation of the other


from typing import *
import unittest
import time
from collections import defaultdict

'''
Ideas:
1. a permutation is essentially a rearrangedment of characters
2. What is character Set? assume ASCII 128
3. 1 array size 128 and the sum should be 0 at the end O(N)
4. sort then comapre O(NlogN)
5. 1 array size 128 increment for first str decrement for second str if ever negative return false
'''

#O(N)
def is_permutation(s1, s2):
    if(len(s1) != len(s2)):
        return False

    chars = [0] * 128
    for c in s1:
        chars[ord(c)] += 1
    
    for c in s2:
        val = ord(c)
        if chars[val] == 0:
            return False
        chars[val] -= 1
    
    return True

#O(N)
#probably worse than other method
def is_permutation_sum(s1, s2):
    if(len(s1) != len(s2)):
        return False

    chars = [0] * 128

    for i in range(len(s1)):
        chars[ord(s1[i])] += 1
        chars[ord(s2[i])] -= 1

    
    return sum(chars) == 0

#Python Way
def is_permutation_python(s1, s2):
    if(len(s1) != len(s2)):
        return False

    return Counter(s1) == Counter(s2)

class Test(unittest.TestCase):
    # str1, str2, is_permutation
    test_cases = (
        ("dog", "god", True),
        ("abcd", "bacd", True),
        ("3563476", "7334566", True),
        ("wef34f", "wffe34", True),
        ("dogx", "godz", False),
        ("abcd", "d2cba", False),
        ("2354", "1234", False),
        ("dcw4f", "dcw5f", False),
        ("DOG", "dog", False),
        ("dog ", "dog", False),
        ("aaab", "bbba", False),
    )

    testable_functions = [
        is_permutation,
        is_permutation_sum,
        is_permutation_python
    ]

    def test_cp(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)

        # true check
        for check_permutation in self.testable_functions:
            start = time.perf_counter()
            for str1, str2, expected in self.test_cases:
                assert (check_permutation(str1, str2) == expected, f"{check_permutation.__name__} failed for values: {str1} {str2}" )
                function_runtimes[check_permutation.__name__] += (
                        time.perf_counter() - start
                    ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name}: {runtime:.1f}ms")


if __name__ == "__main__":
    unittest.main()