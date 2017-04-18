"""
:Author: Pravallika
:Description: Given a binary tree, return all root-to-leaf paths.
:Explanation: For example, given the following binary tree:

		   1
		 /   \
		2     3
 		\
  		 5
		
		All root-to-leaf paths are:
		
		["1->2->5", "1->3"]


"""


class TreeNode(object):
	
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		
	def __repr__(self):
		return "{}".format(self.val)


class BinaryTree(object):
	
	def printPaths(self, root):
		
		"""
		:type root: TreeNode
		:rtype: List[str]
		"""
		result = []
		path = []
		
		self.printPathUtil(root, result, path)
		return result

	def printPathUtil(self, node, result, path):
		if node is None:
			return

		if node.left is node.right is None:
			ans = ""
			for n in path:
				ans += str(n.val)+"->"
			result.append(ans+str(node.val))

		if node.left:
			path.append(node)
			self.printPathUtil(node.left, result, path)
			path.pop()

		if node.right:
			path.append(node)
			self.printPathUtil(node.right, result, path)
			path.pop()



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

obj = BinaryTree()

print(obj.printPaths(root))
