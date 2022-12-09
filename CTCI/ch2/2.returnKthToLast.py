from linkedList import LinkedList
from typing import *

def kth_to_last(n: LinkedList, k : int):
  curr = last = n.head
  for i in range(k - 1):
    if(last == None):
      return None
    last = last.next
  
  while (last.next):
    curr = curr.next
    last = last.next
  return curr


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

test_cases = (
    # list, k, expected
    ((10, 20, 30, 40, 50), 1, 50),
    ((10, 20, 30, 40, 50), 5, 10),
)


def test_kth_to_last():
    for linked_list_values, k, expected in test_cases:
        ll = LinkedList(linked_list_values)
        res = kth_to_last(ll, k).value
        
        print(res)
        assert res == expected
        # assert kth_last_recursive(ll, k).value == expected


if __name__ == "__main__":
    test_kth_to_last()