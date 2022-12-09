from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    end = head
    dummy = ListNode(0, head)
    nth = dummy
        
    for _ in range(n):
        end = end.next
    
    
    while end:
        nth = nth.next
        end = end.next
        
    nth.next = nth.next.next
    return dummy.next