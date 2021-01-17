# Reverse a stack.


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, val):
        node = Node(val)
        node.next = self.top
        self.top = node

    def is_empty(self):
        return not self.top

    def pop(self):
        if not self.is_empty():
            val = self.top.val
            self.top = self.top.next
            return val

    def reverse(self):
        if not self.is_empty():
            # To reverse a stack, just put it into another stack.
            new_stack = Stack()
            top = self.top
            while top:
                new_stack.push(top.val)
                top = top.next
            self.top = new_stack.top

    def print_stack(self):
        top = self.top
        while top:
            print(top.val, end=', ')
            top = top.next
        print("\n")

s = Stack()
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.print_stack()
s.reverse()
s.print_stack()
print(s.pop())
s.print_stack()

"""
Output:
6, 5, 4, 3, 2, 

2, 3, 4, 5, 6, 

2
3, 4, 5, 6, 
"""
