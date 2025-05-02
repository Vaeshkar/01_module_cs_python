###################################
# In-Order Traversal (Ascending Order for BST)
###################################

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root_value):
        self.root = BSTNode(root_value)

    def insert(self, value):
        """Insert a new value into the BST."""
        self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = BSTNode(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:  # value >= current_node.value goes to the right
            if current_node.right is None:
                current_node.right = BSTNode(value)
            else:
                self._insert_recursive(current_node.right, value)

    def in_order_traversal(self, node, visit_list):
        """In-order yields ascending order for a BST."""
        if node is None:
            return
        self.in_order_traversal(node.left, visit_list)
        visit_list.append(node.value)
        self.in_order_traversal(node.right, visit_list)

bst = BinarySearchTree(10)
bst.insert(5)
bst.insert(15)
bst.insert(2)
bst.insert(7)
bst.insert(9)
bst.insert(20)
bst.insert(12)
bst.insert(18)

values = []
bst.in_order_traversal(bst.root, values)
print("In-order traversal (sorted):", values)
# Expected output: In-order traversal (sorted): [2, 5, 7, 9, 10, 12, 15, 18, 20]   

###################################
# Insertion
###################################

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root_value):
        self.root = BSTNode(root_value)

    def insert(self, value):
        """Insert a new value into the BST."""
        self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = BSTNode(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:  # value >= current_node.value goes to the right
            if current_node.right is None:
                current_node.right = BSTNode(value)
            else:
                self._insert_recursive(current_node.right, value)

    def in_order_traversal(self, node, visit_list):
        """In-order yields ascending order for a BST."""
        if node is None:
            return
        self.in_order_traversal(node.left, visit_list)
        visit_list.append(node.value)
        self.in_order_traversal(node.right, visit_list)

bst = BinarySearchTree(10)
bst.insert(5)
bst.insert(15)
bst.insert(2)
bst.insert(7)
bst.insert(9)
bst.insert(20)
bst.insert(12)
bst.insert(18)

values = []
bst.in_order_traversal(bst.root, values)
print("In-order traversal (sorted):", values)
# Expected output: In-order traversal (sorted): [2, 5, 7, 9, 10, 12, 15, 18, 20]   

###################################
# Searching
###################################

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root_value):
        self.root = BSTNode(root_value)

    def insert(self, value):
        """Insert a new value into the BST."""
        self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = BSTNode(value)
            else:
                self._insert_recursive(current_node.left, value)
        else: # value >= current_node.value goes to the right
            if current_node.right is None:
                current_node.right = BSTNode(value)
            else:
                self._insert_recursive(current_node.right, value)
                
    def search(self, value):
        """
        Search for 'value' starting from the root.
        Return True if found, False otherwise.
        """
        current = self.root
        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False


bst = BinarySearchTree(10)
bst.insert(5)
bst.insert(15)
bst.insert(2)
bst.insert(7)
bst.insert(9)
bst.insert(20)
bst.insert(12)
bst.insert(18)

print(bst.search(5)) # Expected: True
print(bst.search(50)) # Expected: False

###################################
# Find lowest
###################################

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root_value):
        self.root = BSTNode(root_value)

    def insert(self, value):
        """Insert a new value into the BST."""
        self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = BSTNode(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:  # value >= current_node.value goes to the right
            if current_node.right is None:
                current_node.right = BSTNode(value)
            else:
                self._insert_recursive(current_node.right, value)

    def in_order_traversal(self, node, visit_list):
        """In-order yields ascending order for a BST."""
        if node is None:
            return
        self.in_order_traversal(node.left, visit_list)
        visit_list.append(node.value)
        self.in_order_traversal(node.right, visit_list)
    
    def _find_min(self, node):
        """
        Find the node with the minimum value in this subtree
        by going left as far as possible.
        """
        current = node
        while current.left is not None:
            current = current.left
        return current

bst = BinarySearchTree(10)
bst.insert(5)
bst.insert(15)
bst.insert(2)
bst.insert(7)
bst.insert(9)
bst.insert(20)
bst.insert(12)
bst.insert(18)

values = []
bst.in_order_traversal(bst.root, values)
print("In-order traversal (sorted):", values)
# Expected output: In-order traversal (sorted): [2, 5, 7, 9, 10, 12, 15, 18, 20]  

###################################
# Delete
################################### 

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root_value):
        self.root = BSTNode(root_value)

    def insert(self, value):
        """Insert a new value into the BST."""
        self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = BSTNode(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:  # value >= current_node.value goes to the right
            if current_node.right is None:
                current_node.right = BSTNode(value)
            else:
                self._insert_recursive(current_node.right, value)

    def in_order_traversal(self, node, visit_list):
        """In-order yields ascending order for a BST."""
        if node is None:
            return
        self.in_order_traversal(node.left, visit_list)
        visit_list.append(node.value)
        self.in_order_traversal(node.right, visit_list)
    
    def delete(self, value):
        """
        Delete 'value' from the tree if it exists.
        """
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        """
        Returns the (possibly new) root of the subtree after deletion.
        """
        if node is None:
            return None  # value not found, do nothing

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Found the node to delete
            # Case 1: no children
            if node.left is None and node.right is None:
                node = None
            # Case 2: one child
            elif node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            # Case 3: two children
            else:
                # Find in-order successor (minimum in right subtree)
                successor = self._find_min(node.right)
                # Swap values with successor
                node.value = successor.value
                # Delete successor from right subtree
                node.right = self._delete_recursive(node.right, successor.value)

        return node

    def _find_min(self, node):
        """
        Find the node with the minimum value in this subtree
        by going left as far as possible.
        """
        current = node
        while current.left is not None:
            current = current.left
        return current

bst = BinarySearchTree(10)
bst.insert(5)
bst.insert(15)
bst.insert(2)
bst.insert(7)
bst.insert(9)
bst.insert(20)
bst.insert(12)
bst.insert(18)

values = []
bst.in_order_traversal(bst.root, values)
print("First in-order traversal (sorted):", values) # Expected output: In-order traversal (sorted): [2, 5, 7, 9, 10, 12, 15, 18, 20]   
bst.delete(10)
values = []
bst.in_order_traversal(bst.root, values)
print("Second in-order traversal (sorted):", values) # Expected output: Second in-order traversal (sorted): [2, 5, 7, 9, 12, 15, 18, 20]
