"""
:Author: Pravallika
:Description: Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer,
		
		 or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

		Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. 
	
		You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
"""


class TreeNode(object):
	
	def __init__(self,x):
		
		self.val = x
		self.left = None
		self.right = None

class SerializeDe(object):
	
	def serialize(self,root):
		
		"""
		:type root: TreeNode
		:rtypr: str
		"""
		
		def serializeHelper(root):
			
			if root:
				vals.append(str(root.val))
				serializeHelper(root.left)
				serializeHelper(root.right)
			else:
				vals.append('#')
			
		vals = []
		return ' '.join(vals)


	def deserialize(self, data):
		
		"""
		:type data: str
		:rtype: TreeNode
		"""
		
		def deserializeHelper():
		
			val = next(vals)
			
			if val == '#':
				return None
			Node = TreeNode(val)
			Node.left = deserializeHelper()
			Node.right = deserializeHelper()
			return Node
		
		vals = iter(data.split())
		return deserializeHelper()



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

obj = SerializeDe()
data = obj.serialize(root)
print(data)
#print(obj.deserialize(data))
