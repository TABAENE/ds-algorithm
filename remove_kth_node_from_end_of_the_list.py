# Remove Kth node from end of the list.
# Use one slow and one fast pointer.


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def add(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

    def remove_kth_node_from_end(self, kth_node):
        start = 1
        slow_pointer = self.head
        fast_pointer = self.head
        # We can do this without using second variable start
        # kth_node > 0; kth_node -= 1
        while start <= kth_node and fast_pointer:
            fast_pointer = fast_pointer.next
            start += 1
        if start - 1 == kth_node:
            # on reaching last element fast_pointer.next would be None.
            # If we don't have fast_pointer.next then at last iteration fast pointer will
            # not moved (because it will set to None) and slow pointer will get moved by one.
            while fast_pointer and fast_pointer.next:
                slow_pointer = slow_pointer.next
                fast_pointer = fast_pointer.next
            slow_pointer.next = fast_pointer
            return "{}th element removed".format(kth_node)
        return "{}th element not found in list".format(kth_node)

    def print_list(self):
        head = self.head
        while head:
            print(head.val, end='   ')
            head = head.next
        print("\n")


linked_list = LinkedList()
linked_list.add(5)
linked_list.add(10)
linked_list.add(15)
linked_list.add(20)
linked_list.add(25)
linked_list.print_list()
print(linked_list.remove_kth_node_from_end(2))
linked_list.print_list()

"""
Output:
25   20   15   10   5   

2th element removed
25   20   15   5 
"""
