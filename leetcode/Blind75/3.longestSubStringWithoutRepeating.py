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

    
    def lengthOfLongestSubstring(self, s):
        if(len(s) == 1):
            return 1
        
        l = 0
        r = 0
        
        dict = {}
        maxLen = 0
        while r < len(s):
            if s[r] in dict:
                l = max(dict[s[r]], l)
            
            curr = r - l + 1
            maxLen = max(curr, maxLen)
            dict[s[r]] = r + 1
            r += 1
        
        return maxLen

    
    def lengthOfLongestSubstring(self, s):
        charSet = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res