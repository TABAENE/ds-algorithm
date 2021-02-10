# Amazon: Level order traversal of a tree is breadth first traversal for the tree.


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear

    def push(self, val):
        if not self.rear and not self.front:
            self.rear = Node(val)
            self.front = self.rear
            return
        self.rear.next = Node(val)
        self.rear = self.rear.next

    def pop(self):
        if not self.front and not self.rear:
            return
        elif self.front == self.rear:
            temp = self.front
            self.front = None
            self.rear = None
            return temp.val
        temp = self.front
        self.front = self.front.next
        return temp.val

    def print_list(self):
        temp = self.front
        while temp:
            print (temp.val)
            temp = temp.next


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root=None):
        self.root = root
        self.bft = []

    @staticmethod
    def breadth_first_traversal(root):
        if not root:
            return
        traversed_node = []
        linked_list = LinkedList()
        linked_list.push(root)
        while linked_list.front:
            temp = linked_list.pop()
            if temp:
                traversed_node.append(temp.val)
                if temp.left:
                    linked_list.push(temp.left)
                if temp.right:
                    linked_list.push(temp.right)
        return traversed_node

    def print_tree(self, current_node):
        if not current_node:
            return
        print(current_node.val)
        self.print_tree(current_node.left)
        self.print_tree(current_node.right)


bt2 = BinaryTree()
one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
bt2.root = one
one.left = three
one.right = two
three.left = TreeNode(5)
three.right = TreeNode(4)
two.left = TreeNode(6)

print ("Level order traversal.", BinaryTree.breadth_first_traversal(bt2.root))

# OP: Level order traversal. [1, 3, 2, 5, 4, 6]
