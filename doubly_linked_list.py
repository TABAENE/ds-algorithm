
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def add(self, val):
        node = Node(val)
        node.next = self.head
        if self.head:
            self.head.previous = node
        self.head = node

    def insert_after(self, node_val, val):
        node = Node(val)
        head = self.head
        while head:
            if head.val == node_val:
                temp = head.next
                head.next = node
                node.previous = head
                node.next = temp
                temp.previous = node
                return "Node inserted successfully..."
            head = head.next
        return "node with given value does not exist"

    def delete(self):
        self.head = self.head.next
        self.head.previous = None

    def remove(self, val):
        head = self.head
        if head.val == val:
            self.head = self.head.next
        # while head.next:
        #     if head.next.val == val:
        #         head.next = head.next.next
        #         break
        #     head = head.next
        while head:
            if head.val == val:
                head.previous.next = head.next
                # last element next would be None
                if head.next:
                    head.next.previous = head.previous
                return True
            head = head.next
        return False

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


linked_list = DoublyLinkedList()
linked_list.add(5)
linked_list.add(10)
linked_list.add(15)
linked_list.insert_after(10, 100)
linked_list.remove(5)
linked_list.print_list()

# Output:
# 15
# 10
# 100
