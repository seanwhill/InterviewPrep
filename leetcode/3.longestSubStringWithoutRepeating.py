# Given a string s, find the length of the longest substring without repeating characters.

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

class Solution:
    def lengthOfLongestSubstring(self, s):
        dct = {}
        start = maxLen = 0
        
        for end, value in enumerate(s):
            if value in dct:
                start = max(dct[value], start)
                
            curr = end - start + 1
            maxLen = max(curr, maxLen)
            dct[value] = end + 1

        return maxLen