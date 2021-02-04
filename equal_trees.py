# Facebook/Google: Find if two binary search trees are equal ?


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def __init__(self):
        self.root = None
        self.visited_nodes = []

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

    def in_order_traversal(self, root):

        if not root:
            return
        self.in_order_traversal(root.left)
        self.visited_nodes.append(root.val)
        self.in_order_traversal(root.right)

    def is_equal(self, tree):
        # Two trees are equal if both in order traversal result in same list of nodes.
        if self.visited_nodes == tree.visited_nodes:
            print("Trees are equal.")
        else:
            print("Trees are NOT equal.")


# Tree 1
bt1 = BinaryTree()
bt1.add(4, bt1.root)
bt1.add(3, bt1.root)
bt1.add(6, bt1.root)

# Tree 2
bt2 = BinaryTree()
bt2.add(6, bt2.root)
bt2.add(3, bt2.root)
bt2.add(4, bt2.root)
# bt.print_tree(bt.root)

bt1.in_order_traversal(bt1.root)
bt2.in_order_traversal(bt2.root)

bt1.is_equal(bt2)

"""
Trees are equal.
"""
