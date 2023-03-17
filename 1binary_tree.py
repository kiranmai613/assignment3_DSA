#Implement Binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add_node(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        queue = [self.root]
        while queue:
            current_node = queue.pop(0)
            if current_node.left is None:
                current_node.left = new_node
                break
            elif current_node.right is None:
                current_node.right = new_node
                break
            else:
                queue.append(current_node.left)
                queue.append(current_node.right)

    def print_tree(self):
        if self.root is None:
            print("Tree is empty")
            return
        queue = [self.root]
        while queue:
            current_node = queue.pop(0)
            print(current_node.data)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
# Create a new Binary Tree
tree = BinaryTree()

# Add some nodes to the tree
tree.add_node(1)
tree.add_node(2)
tree.add_node(3)
tree.add_node(4)
tree.add_node(5)

# Print the tree
tree.print_tree()
