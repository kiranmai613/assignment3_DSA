class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def pre_order_traversal(node):
    if node is not None:
        print(node.value, end=', ')
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)
        print(node.value, end=', ')
        in_order_traversal(node.right)

def post_order_traversal(node):
    if node is not None:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.value, end=', ')

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(2)

print("Pre-order traversal:")
pre_order_traversal(root)
print()

print("In-order traversal:")
in_order_traversal(root)
print()

print("Post-order traversal:")
post_order_traversal(root)
print()

