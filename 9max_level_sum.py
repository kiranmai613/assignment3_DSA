class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_level_sum(root):
    if not root:
        return 0

    # Initialize a queue to perform level-order traversal of the tree
    queue = []
    queue.append(root)
    max_sum = float('-inf')

    while queue:
        size = len(queue)
        level_sum = 0

        # Process all nodes at current level
        for i in range(size):
            node = queue.pop(0)
            level_sum += node.val

            # Add the left and right children to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Update the maximum level sum if the current level sum is greater
        max_sum = max(max_sum, level_sum)

    return max_sum

# Example usage
root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(0)
root.left.left = TreeNode(7)
root.left.right = TreeNode(-8)

print("Maximum level sum:", max_level_sum(root))
