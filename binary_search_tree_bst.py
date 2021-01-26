# Binary Search Tree


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None


    def find_node(self, val):
        temp = self.root
        while temp:
            if val < temp.val:
                if not temp.left:
                    return None
                temp = temp.left
            elif val > temp.val:
                if not temp.right:
                    return None
                temp = temp.right
            else:
                return temp
        return None

    def find_node_with_recursion(self, start, val):
        if val < start.val:
            if not start.left:
                return None
            self.find_node_with_recursion(start.left, val)
        elif val > start.val:
            if not start.right:
                return None
            self.find_node_with_recursion(start.right, val)
        return start

    def add_with_recursion(self, start, val):

        if not self.root:
            self.root = TreeNode(val)
            return True

        if val < start.val:
            if not start.left:
                start.left = TreeNode(val)
                return True
            self.add_with_recursion(start.left, val)
        elif val > start.val:
            if not start.right:
                start.right = TreeNode(val)
                return True
            self.add_with_recursion(start.right, val)
        # else:
        #     # TODO: where duplicate should go?
        #     if not start.right:
        #         start.right = TreeNode(val)
        #         return True
        #     self.add_with_recursion(start.right, val)
        return False

    def add(self, val):
        node = TreeNode(val)

        if not self.root:
            self.root = node
            return

        temp = self.root
        while temp:
            if node.val < temp.val:
                if not temp.left:
                    temp.left = node
                    break
                temp = temp.left
            else:
                if not temp.right:
                    temp.right = node
                    break
                temp = temp.right

        return True

    def delete_node(self, root, val):

        if not root:
            return

        if val < root.val:
            root.left = self.delete_node(root.left, val)
        elif val > root.val:
            root.right = self.delete_node(root.right, val)
        else:
            # We found the value to be deleted.

            # If there is no left child.
            if not root.left:
                return root.right

            # If there is no right child.
            if not root.right:
                return root.left

            # If both left and right children exist in the node then replace its value with
            # the minimum value in the right subtree. Now delete that minimum node in the right subtree.
            temp = root.right
            while temp.left:
                temp = temp.left
            temp.val, root.val = root.val, temp.val

            root.right = self.delete_node(root.right, temp.val)

        return root


    def print_tree(self, node):
        if not node:
            return 0
        print(node.val, node.left, node.right, end='\n')
        self.print_tree(node.left)
        self.print_tree(node.right)


bt = BinaryTree()
# bt.add(12)
# bt.add(6)
# bt.add(8)
# print("Find node", bt.find_node(8))
bt.add_with_recursion(bt.root, 50)
bt.add_with_recursion(bt.root, 35)
bt.add_with_recursion(bt.root, 81)
bt.add_with_recursion(bt.root, 40)
bt.add_with_recursion(bt.root, 20)
bt.add_with_recursion(bt.root, 18)
bt.add_with_recursion(bt.root, 91)
bt.add_with_recursion(bt.root, 15)
bt.add_with_recursion(bt.root, 75)
print("TREE!!!!!!!!!!!!\n")
bt.print_tree(bt.root)
# print("Find node", bt.find_node_with_recursion(bt.root, 8))
# print("Find node", bt.find_node_with_recursion(bt.root, 88))
print("TREE AFTER DELETION of node {}!!!!!!!!!!!!\n".format(15))
print ("delete node", bt.delete_node(bt.root, 15))
bt.print_tree(bt.root)

"""
O/P:
TREE!!!!!!!!!!!!

50 <__main__.TreeNode object at 0x00BB6058> <__main__.TreeNode object at 0x00BB61C0>
35 <__main__.TreeNode object at 0x00BB6118> <__main__.TreeNode object at 0x00BB6100>
20 <__main__.TreeNode object at 0x00BB6160> None
18 <__main__.TreeNode object at 0x00BB61F0> None
15 None None
40 None None
81 <__main__.TreeNode object at 0x00BB6220> <__main__.TreeNode object at 0x00BB60B8>
75 None None
91 None None
TREE AFTER DELETION of node 15!!!!!!!!!!!!

delete node <__main__.TreeNode object at 0x00BB6040>
50 <__main__.TreeNode object at 0x00BB6058> <__main__.TreeNode object at 0x00BB61C0>
35 <__main__.TreeNode object at 0x00BB6118> <__main__.TreeNode object at 0x00BB6100>
20 <__main__.TreeNode object at 0x00BB6160> None
18 None None
40 None None
81 <__main__.TreeNode object at 0x00BB6220> <__main__.TreeNode object at 0x00BB60B8>
75 None None
91 None None
"""
