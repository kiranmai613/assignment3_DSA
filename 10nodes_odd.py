class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_odd_level(root):
    if not root:
        return

    # Initialize a queue to perform level-order traversal of the tree
    queue = []
    queue.append(root)
    level = 1

    while queue:
        size = len(queue)

        # Process all nodes at current level
        for i in range(size):
            node = queue.pop(0)

            # If the current level is odd, print the node value
            if level % 2 == 1:
                print(node.val, end=" ")

            # Add the left and right children to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Move to the next level
        level += 1

# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("Nodes at odd levels:")
print_odd_level(root)
