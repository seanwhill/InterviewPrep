# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = curr = ListNode(0)
        carry = 0

        while(l1 or l2 or carry):
            val = 0 
            if(l1):
                val += l1.val
                l1 = l1.next
            if(l2):
                val += l2.val
                l2 = l2.next
            val += carry
            carry = val // 10
            val = val % 10
            
            curr.next = ListNode(val)
            curr = curr.next
        
        return res.next
            

