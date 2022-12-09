# Definition for singly-linked list.

from typing import *

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        curr, ahead = head, head
        
        while ahead and ahead.next:
            curr = curr.next
            ahead = ahead.next.next
            
            if curr == ahead:
                return True

    
        
        return False