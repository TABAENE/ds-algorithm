
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

    def delete(self):
        self.head = self.head.next

    def remove(self, val):
        head = self.head
        if head.val == val:
            self.head = self.head.next
        while head.next:
            if head.next.val == val:
                head.next = head.next.next
                break
            head = head.next

    def find(self, val):
        head = self.head
        while head:
            if head.val == val:
                return True
            head = head.next
        return False

    def print_list(self):
        head = self.head
        while head:
            print(head.val)
            head = head.next


linked_list = LinkedList()
linked_list.add(5)
linked_list.add(10)
linked_list.add(15)
linked_list.remove(18)
linked_list.delete()
print(linked_list.find(10))
linked_list.print_list()

# Output:
# True
# 10
# 5
