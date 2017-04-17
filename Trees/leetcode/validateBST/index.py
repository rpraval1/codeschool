"""
:Author: Pravallika
:Description: Given a binary tree, determine if it is a valid binary search tree (BST).

		Assume a BST is defined as follows:

		- The left subtree of a node contains only nodes with keys less than the node's key.
		- The right subtree of a node contains only nodes with keys greater than the node's key.
		- Both the left and right subtrees must also be binary search trees.
:Explanation:  
		  2
   		 / \
		1   3
	Binary tree [2,1,3], return true.

"""


class TreeNode(object):
	
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None


class ValidBST(object):
	
	def isValid(self, root):
		return self.isValidUtil(root, float("-inf"), float("inf"))

	def isValidUtil(self, root, min, max):
		if root is None:
			return True
		
		if root.val < min or root.val > max:
			return False
		
		return (self.isValidUtil(root.left, min, root.val-1) and self.isValidUtil(root.right, root.val+1, max))


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

obj = ValidBST()

print(obj.isValid(root))
