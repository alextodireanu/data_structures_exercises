# implementation of a binary tree structure
# primary note is called ROOT
# last row nodes are called LEAVES
# a node has a pointer for left and right
# a value of a node is called KEY


class Node:
    """Node representation"""
    def __init__(self, key):
        """Node initialization"""
        self.left = None
        self.right = None
        self.val = key


# creating a root
root = Node(1)

# creating the nodes linked to the root
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
