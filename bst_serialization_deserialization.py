# Serialise and de-serialize in binary tree.


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root=None):
        self.root = root
        self.index = 0

    def add(self, start, val):
        if not self.root:
            self.root = Node(val)
            return True

        if val < start.val:
            if not start.left:
                start.left = Node(val)
                return True
            self.add(start.left, val)
        else:
            if not start.right:
                start.right = Node(val)
                return True
            self.add(start.right, val)

    def serialize(self, root, serialised_list):
        if not root:
            serialised_list.append(-1)
            return
        serialised_list.append(root.val)
        self.serialize(root.left, serialised_list)
        self.serialize(root.right, serialised_list)

    def de_serialize(self, serialised_tree):
        if not self.index:
            self.index = 0
        if self.index > len(serialised_tree) - 1 or serialised_tree[self.index] == -1:
            self.index += 1
            return
        new_node = Node(serialised_tree[self.index])
        self.index += 1
        new_node.left = self.de_serialize(serialised_tree)
        new_node.right = self.de_serialize(serialised_tree)
        return new_node

    def print_tree(self, current_node):
        if not current_node:
            return
        print(current_node.val)
        self.print_tree(current_node.left)
        self.print_tree(current_node.right)


bt = BinaryTree()
bt.add(bt.root, 1)
bt.add(bt.root, 3)
bt.add(bt.root, 2)
bt.add(bt.root, 5)
bt.add(bt.root, 4)
bt.print_tree(bt.root)
serialised_tree = []
bt.serialize(bt.root, serialised_tree)
print ("serialized tree.", serialised_tree)
print ("De-Serialization ....\n")
node = bt.de_serialize(serialised_tree)
bt.print_tree(node)
