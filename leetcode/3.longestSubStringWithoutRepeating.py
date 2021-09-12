# Given a string s, find the length of the longest substring without repeating characters.

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

class Solution:
    def lengthOfLongestSubstring(self, s):
        dict = {}
        max = start = 0

        for i,character in enumerate(s):
            if dict[character] > start:
                start = dict[character] + 1
            curr = i - start + 1
            if curr > max:
                max = curr
            dict[character] = 1

        return max