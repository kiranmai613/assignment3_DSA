class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs_traversal(root):
    if root is None:
        return
    
    queue = [root]
    while queue:
        current_node = queue.pop(0)
        print(current_node.value, end=" ")
        if current_node.left is not None:
            queue.append(current_node.left)
        if current_node.right is not None:
            queue.append(current_node.right)
            
def dfs_traversal(root):
    if root is None:
        return
    
    stack = [root]
    while stack:
        current_node = stack.pop()
        print(current_node.value, end=" ")
        if current_node.right is not None:
            stack.append(current_node.right)
        if current_node.left is not None:
            stack.append(current_node.left)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("BFS Traversal:")
bfs_traversal(root)  # prints 1 2 3 4 5

print("\nDFS Traversal:")
dfs_traversal(root)  # prints 1 3 5 4 2
