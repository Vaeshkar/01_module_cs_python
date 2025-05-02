class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Pre-Order Traversal (Root -> Left -> Right)
def pre_order_traversal(root):
    if root:
        print(root.value, end=" ")  # Visit root
        pre_order_traversal(root.left)  # Recur on left
        pre_order_traversal(root.right)  # Recur on right

# In-Order Traversal (Left -> Root -> Right)
def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)  # Recur on left
        print(root.value, end=" ")  # Visit root
        in_order_traversal(root.right)  # Recur on right

# Post-Order Traversal (Left -> Right -> Root)
def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)  # Recur on left
        post_order_traversal(root.right)  # Recur on right
        print(root.value, end=" ")  # Visit root

# Level-Order Traversal (BFS - Level by Level)
from collections import deque
def level_order_traversal(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Build the tree
root = TreeNode("A")
root.left = TreeNode("B")
root.right = TreeNode("C")
root.left.left = TreeNode("D")
root.left.right = TreeNode("E")
root.right.right = TreeNode("F")

# Call traversal functions
print("Pre-Order Traversal:")
pre_order_traversal(root)  # Output: A B D E C F

print("\n\nIn-Order Traversal:")
in_order_traversal(root)  # Output: D B E A C F

print("\n\nPost-Order Traversal:")
post_order_traversal(root)  # Output: D E B F C A

print("\n\nLevel-Order Traversal:")
level_order_traversal(root)  # Output: A B C D E F
