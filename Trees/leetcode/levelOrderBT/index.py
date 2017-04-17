"""
:Author: Pravallika
:Description: Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
:Explanation: For example:
		
		Given binary tree [3,9,20,null,null,15,7]
		
		    3
   		   / \
  		  9  20
    		    /  \
   		   15   7
		
		return its level order traversal as:
 		
		
		[
  			[3],
  			[9,20],
  			[15,7]
		]
"""

class TreeNode(object):

	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

	def __repr__(self):
		if self:
			return "{}".format(self.val)


class BinaryTree(object):

	def levelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		
		if root is None:
			return []

		result = []
		current = [root]
		
		while current:
			nextLevel = []
			vals = []

			for node in current:
				vals.append(node.val)
				if node.left:
					nextLevel.append(node.left)
				if node.right:
					nextLevel.append(node.right)

			current  = nextLevel
			result.append(vals)

		return result



root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

obj = BinaryTree()
print(obj.levelOrder(root))
