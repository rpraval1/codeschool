"""
:Author: Pravallika
:Description: Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

		If two nodes are in the same row and column, the order should be from left to right.
:Explanation: Given binary tree [3,9,20,null,null,15,7]
		
		 3
		 /\
		/  \
		9  20
		    /\
		   /  \
		  15   7

		return its vertical order traversal as:

		[
  			[9],
			[3,15],
			[20],
			[7]
		]

"""
import collections

class TreeNode(object):

	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		
	def __repr__(self):
		if self:
			return "{}".format(self.val)

class VerticalOrder(object):
	
	def printVerticalOrder(self, root):
		
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		
		cols = collections.defaultdict(list)
		queue = [(root, 0)]
		
		for node, i in queue:
			if node:
				cols[i].append(node.val)
				queue += (node.left, i-1), (node.right, i+1)
		
		return [cols[i] for i in sorted(cols)] if cols else []



root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

obj = VerticalOrder()

print(obj.printVerticalOrder(root))
