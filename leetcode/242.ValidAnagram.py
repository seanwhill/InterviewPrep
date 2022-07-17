# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

def isAnagram(self, s: str, t: str) -> bool:
    
    if(len(s) != len(t)):
        return False

    visited = [0] * 26
    a_ASCII = ord("a")
    
    for char in s:
        visited[ord(char) - a_ASCII] += 1
    
    for char in t:
        val = ord(char) - a_ASCII
        if(visited[val]) == 0:
            return False
        visited[val] -= 1
        
    return True

def isAnagra2(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    countS, countT = {}, {}
    
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
    return True