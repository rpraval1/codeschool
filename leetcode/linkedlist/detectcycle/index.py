class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None

class Solution(object):
	def detectCycle(self,head):
		if head == None:
		    return False
		
		if head.next == None:
		    return False
	
		ptr1 = head
		ptr2 = ptr1.next
		
		while ptr1:
			if ptr1 == ptr2:
				return True
			if ptr2 == None:
				return False
			ptr2 = ptr2.next
			if ptr1 == ptr2:
				return True
			if ptr2 == None:
				return False
			ptr2 = ptr2.next
			ptr1 = ptr1.next
		return False
			
head = ListNode(2)
head.next = ListNode(3)
head.next.next = ListNode(5)
head.next.next.next = head.next
solution = Solution()
print(solution.detectCycle(head))		
		
