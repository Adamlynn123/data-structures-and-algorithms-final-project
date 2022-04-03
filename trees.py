# Python program to demonstrate
# insert operation in binary search tree

# A utility class that represents
# an individual node in a BST


class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

# A utility function to insert
# a new node with the given key


def insert(root, value):
	if root is None:
		return Node(value)
	else:
		if root.val == value:
			return root
		elif root.val < value:
			root.right = insert(root.right, value)
		else:
			root.left = insert(root.left, value)
	return root

# A utility function to do inorder tree traversal


def inorder(root):
	if root:
		inorder(root.left)
		print(root.val)
		inorder(root.right)



r = Node(7)
r = insert(r, 2)
r = insert(r, 5)
r = insert(r, 1)
r = insert(r, 9)
r = insert(r, 14)
r = insert(r, 8)

# Inorder traversal
inorder(r)
