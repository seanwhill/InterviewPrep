from linkedList import LinkedListNode
from linkedList import LinkedList

def delete_middle_node(n : LinkedListNode):
  if(n and n.next):
    n.value = n.next.value
    n.next = n.next.next

if __name__ == "__main__":
    ll = LinkedList()
    ll.add_multiple([1, 2, 3, 4])
    middle_node = ll.add(5)
    ll.add_multiple([7, 8, 9])

    print(ll)
    delete_middle_node(middle_node)
    print(ll)