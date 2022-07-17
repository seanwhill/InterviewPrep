import time

from linkedList import LinkedList

def removeDupes(n : LinkedList):
  seen = set()
  curr = n.head
  prev = None
  while (curr) :
    if(curr.value in seen):
      prev.next = curr.next
    else:
      seen.add(curr.value)
      prev = curr
    curr = curr.next
  n.tail = prev
  return n

def removeDupesFollowUp(n:LinkedList):
  curr = runner = n.head
  while(curr != None):
    runner = curr
    while(runner.next != None):
      if(runner.next.value == curr.value):
        runner.next = runner.next.next
      else:
        runner = runner.next
    curr = curr.next
  
  n.tail = runner
  return n

testable_functions = (removeDupes, removeDupesFollowUp)
test_cases = (
    ([], []),
    ([1, 1, 1, 1, 1, 1], [1]),
    ([1, 2, 3, 2], [1, 2, 3]),
    ([1, 2, 2, 3], [1, 2, 3]),
    ([1, 1, 2, 3], [1, 2, 3]),
    ([1, 2, 3], [1, 2, 3]),
)


def test_remove_dupes():
    for f in testable_functions:
        start = time.perf_counter()
        for _ in range(100):
            for values, expected in test_cases:
                expected = expected.copy()
                x = LinkedList(values)
                deduped = f(x)
                assert deduped.values() == expected
              
                deduped.add(5)
                expected.append(5)
                assert deduped.values() == expected

        duration = time.perf_counter() - start
        print(f"{f.__name__} {duration * 1000:.1f}ms")


def example():
    ll = LinkedList.generate(100, 0, 9)
    print(ll)
    removeDupes(ll)
    print(ll)

    ll = LinkedList.generate(100, 0, 9)
    print(ll)
    removeDupesFollowUp(ll)
    print(ll)


if __name__ == "__main__":
    test_remove_dupes()