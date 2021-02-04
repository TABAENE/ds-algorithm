# Amazon: Find path between two Nodes.


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def __init__(self):
        self.root = None
        self.visited_node = []
        self.steps = 0

    def find_path_between_two_node(self):
        pass

    def add(self, val, root):

        if not self.root:
            self.root = TreeNode(val)
            return True

        if val < root.val:
            if not root.left:
                root.left = TreeNode(val)
            self.add(val, root.left)

        elif val > root.val:
            if not root.right:
                root.right = TreeNode(val)
            self.add(val, root.right)

        return True

    def print_tree(self, root):
        if not root:
            return
        print(root.val, root.left, root.right)
        self.print_tree(root.left)
        self.print_tree(root.right)

    def find_path(self, search_val, root):
        if root.val not in self.visited_node:
            self.steps += 1
            self.visited_node.append(root.val)
        else:
            self.steps -= 1
        if root.val == search_val:
            return
        if search_val < root.val:
            self.find_path(search_val, root.left)
        if search_val > root.val:
            self.find_path(search_val, root.right)


bt = BinaryTree()
bt.add(50, bt.root)
bt.add(35, bt.root)
bt.add(81, bt.root)
bt.add(20, bt.root)
bt.add(40, bt.root)
bt.add(75, bt.root)
bt.add(91, bt.root)
bt.add(18, bt.root)
bt.add(15, bt.root)
bt.add(13, bt.root)
bt.add(25, bt.root)
# bt.print_tree(bt.root)
bt.find_path(75, bt.root)
bt.find_path(91, bt.root)
print ("Path between node 75 and 91", bt.steps)
print ("Visited nodes", bt.visited_node)

"""
Path between node 75 and 91 2
Visited nodes [50, 81, 75, 91]
"""
