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
		
		3 9 20 15 7

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

	def printLevelOrder(self, root):
		"""
		:type root: TreeNode 
		:rtype: void

		"""
		
		if root is None:
			return
		
		queue = []
		queue.append(root)

		while(len(queue)>0):
			print(queue[0].val, end=" ")
			node = queue.pop(0)

			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)
			

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

obj = BinaryTree()
obj.printLevelOrder(root)
