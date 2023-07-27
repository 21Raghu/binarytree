class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def insert_node(root, data):
    if root is None:
        return Node(data)
    else:
        if data == root.val:
            return root
        if data > root.val:
            root.right = insert_node(root.right, data)
        else:
            root.left = insert_node(root.left, data)
#
#
def print_node(root):
    if root:
        print(root.val)
        print_node(root.left)
        print_node(root.right)

#
r = insert_node(None, 10)
insert_node(r, 9)
insert_node(r, 11)
print_node(r)
