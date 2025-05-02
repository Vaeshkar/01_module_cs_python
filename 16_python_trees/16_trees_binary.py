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
        if current_node.left is None:
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
            
# -- Now build the tree --

#      R
#     / \
#    A   B
#   / \ / \
#  C  D E  F
#        /
#       G

# 1 create a tree with root 'R'
bt = BinaryTree('R')

# 2 Insert 'A' as left child and 'R', and 'B' as right child of 'R'
bt.insert_left(bt.root, 'A') # nodeA
bt.insert_right(bt.root, 'B') # nodeB

# 3 Get references to the newly inserted nodes for further insertions
nodeA = bt.root.left
nodeB = bt.root.right

# 4 Insert 'C' and 'D' under 'A'
bt.insert_left(nodeA, 'C') #nodeC
bt.insert_right(nodeA, 'D') #nodeD

# 5 Insert 'E' and 'F' under 'B'
bt.insert_left(nodeB, 'E') # nodeE
bt.insert_right(nodeB, 'F') # nodeF

# 6 Get references to the newly inserted nodes for further insertions
# 6 Insert 'G' under 'F' as left child
nodeF = nodeB.right
bt.insert_left(nodeF, 'G') # nodeG

# Test: Access node 'E': which is bt.root(nodeR).right(nodeB).left(nodeE)
print("root.right.left.value:", bt.root.right.left.value) # Output: 'E'