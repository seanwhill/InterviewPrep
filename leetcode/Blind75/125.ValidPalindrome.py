from typing import *

def isPalindrome(self, s: str) -> bool:
    l = 0
    r = len(s) - 1 
    a = ord('a')
    
    
    while l < r:
        if s[l].lower() == s[r].lower():
            l += 1
            r -= 1
        elif (not self.isAlNum(s[l])):
            l += 1
        elif (not self.isAlNum(s[r])):
            r -= 1
        else:
            return False
    
    return True

def isPalindrome(self, s: str) -> bool:
    l = 0
    r = len(s) - 1         
    
    while l < r:
        while (l < r and not self.isAlNum(s[l])):
            l += 1
        while (l < r and not self.isAlNum(s[r])):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    
    return True

def isPalindrome(self, s: str) -> bool:
    res = ""

    for c in s:
        if c.isalnum():
            res += c.lower()
    return res == res[::-1]

def isAlNum(self, c):
    return ( (ord('A') <= ord(c) <= ord('Z'))
            or (ord('a') <= ord(c) <= ord('z'))
            or (ord('0') <= ord(c) <= ord('9')))