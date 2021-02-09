# Google: Check if two trees are mirror.


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    @staticmethod
    def are_mirrors(tree1, tree2):
        if not tree1 and not tree2:
            return True
        if not tree1 or not tree2:
            return False
        return tree1.val == tree2.val and BinaryTree.are_mirrors(tree1.left, tree2.right) and BinaryTree.are_mirrors(tree1.right, tree2.left)

    def print_tree(self, current_node):
        if not current_node:
            return
        print(current_node.val)
        self.print_tree(current_node.left)
        self.print_tree(current_node.right)


bt = BinaryTree()
first = Node(1)
second = Node(2)
third = Node(3)
bt.root = first
first.left = second
first.right = third

bt2 = BinaryTree()
one = Node(1)
two = Node(2)
three = Node(3)
bt2.root = one
one.left = three
one.right = two

print ("Trees are mirrors.", BinaryTree.are_mirrors(bt.root, bt2.root))
