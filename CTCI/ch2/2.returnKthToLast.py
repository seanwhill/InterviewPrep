from linkedList import LinkedList

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