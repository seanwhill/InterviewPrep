# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

#Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

from collections import defaultdict
from typing import *


#Start at beginning, then check if the rest of the arrays are anagrams of it, then exclude them so they don't get reused
# BAD SOLUTION
def groupAnagrams_SLOW(self, strs: List[str]) -> List[List[str]]:
    seen = set()
    res = []
    print(self.isAnagram("eat", "tan"))
    
    for i in range(len(strs)):
        if(strs[i] not in seen):
            subRes = [strs[i]]
            for j in range(i + 1, len(strs)):
                if(self.isAnagram(strs[i], strs[j])):
                    subRes.append(strs[j])
                    seen.add(strs[j])
                    
            res.append(subRes)

        seen.add(strs[i])    
    return res


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    res = defaultdict(list) #CharCount key -> list of anagrams res
    
    for s in strs:
        count = [0] * 26
        
        for c in s:
            count[ord(c) - ord("a")] += 1   
            
        res[tuple(count)].append(s)
                
    return res.values()