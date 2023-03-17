#Function to print all the leaves in a given binary tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_leaves(root):
    if root is not None:
        if root.left is None and root.right is None:
            print(root.value)
        else:
            print_leaves(root.left)
            print_leaves(root.right)
# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Print the leaves of the tree
print_leaves(root)  # prints 4, 5, 6, 7
