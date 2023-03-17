class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_subtrees_with_sum(root, x):
    count = 0
    if not root:
        return 0
    
    def traverse(node):
        nonlocal count
        if not node:
            return 0
        left_sum = traverse(node.left)
        right_sum = traverse(node.right)
        subtree_sum = left_sum + right_sum + node.val
        if subtree_sum == x:
            count += 1
        return subtree_sum
    
    traverse(root)
    return count

root = Node(10)
root.left = Node(5)
root.right = Node(-3)
root.left.left = Node(3)
root.left.right = Node(2)
root.right.right = Node(11)

x = 8
count = count_subtrees_with_sum(root, x)
print("Number of subtrees with sum", x, ":", count)