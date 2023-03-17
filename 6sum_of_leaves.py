class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def sum_of_left_leaves(root):
    def dfs(node, is_left):
        if not node:
            return 0
        if not node.left and not node.right:
            return node.val if is_left else 0
        return dfs(node.left, True) + dfs(node.right, False)
    return dfs(root, False)

# Example usage:
root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)
print(sum_of_left_leaves(root))  # Output: 24 (9 + 15)
