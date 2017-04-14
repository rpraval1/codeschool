class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None
	def __repr__(self):
		if self:
			return "{} -> {}".format(self.val, repr(self.next))

class Solution(object):
	def reverseList(self,head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		if head == None:
			return None
		
		if head.next == None:
			return head
		
		prev = head
		curr = head
		
		while curr:
			temp = curr.next
			if curr == head:
				curr.next = None
			else:
				curr.next = prev
			if temp == None:
				head = curr
			else:
				prev = curr
			curr = temp
		return head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(7)
solution = Solution()
result =  solution.reverseList(head)
print(result)
