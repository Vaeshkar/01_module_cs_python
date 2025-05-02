class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)
        
    def insert_left(self, current_node, new_value):
        new_node = TreeNode(new_value)
        if current_node is None:
            current_node.left = new_node
        else:
            new_node.left = current_node.left
            current_node.left = new_node

    def insert_right(self, current_node, new_value):
        new_node = TreeNode(new_value)
        if current_node.right is None:
            current_node.right = new_node
        else:
            new_node.right = current_node.right
            current_node.right = new_node
            
    def pro_order_traversal(self, start_node, visit_list):
        if start_node is None:
            return
        # 1
        visit_list.append(start_node.value)
        # 2 Traverse left subtree
        self.pro_order_traversal(start_node.left, visit_list)
        # 3 Traverse right subtree
        self.pro_order_traversal(start_node.right, visit_list)

# -- Now build the tree --

#      R
#     / \
#    A   B
#   / \ / \
#  C  D E  F
#        /
#       G

# crea a tree with root 'R'
bt = BinaryTree('R')
            
# Insert 'A' as left child or 'R' and 'B' as right child of 'R'.
bt.insert_left(bt.root, 'A') # nodeA
bt.insert_right(bt.root, 'B') # nodeB

# Get references the the newly inserted nodes for further insertions
nodeA = bt.root.left
nodeB = bt.root.right

# Insert 'E' and 'F' under 'B'
bt.insert_left(nodeA, 'E') # nodeE
bt.insert_right(nodeA, 'F') # nodeF

# Insert 'G' under 'F' as left child
nodeF = nodeB.right
bt.insert_left(bt.root, 'G') # nodeG

# Test Pre-Order Traversal
visit_order = []
bt.pro_order_traversal(bt.root, visit_order)
print("Pre-Order traversal (DFS):", visit_order)