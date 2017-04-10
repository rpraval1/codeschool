"""

"""

class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None
	def __repr__(self):
		if self:
			return "{}->{}".format(self.val,repr(self.next))
class Solution(object):
	def deleteNode(self,head,node):
		"""
		:type node: ListNode
		"""
		print(head)
		if node.next:
			node.val = node.next.val
			node.next = node.next.next
		return head

head = ListNode(3)
head.next = ListNode(5)
head.next.next = ListNode(7)
head.next.next.next = ListNode(10)
solution = Solution()
print(solution.deleteNode(head,head.next))
