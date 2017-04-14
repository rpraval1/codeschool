"""
:Author: Pravallika
:Description: Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
:Explanation: For example,
		Given [3,2,1,5,6,4] and k = 2, return 5.
"""
import random
class LargestElement(object):
	def kthLargest(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		"""
		pivot = random.choice(nums)
		
		nums1 = []
		nums2 = []

		for num in nums:
			if num >= pivot:
				nums1.append(num)
			else:
				nums2.append(num)
		if k<len(nums1):
			return self.kthLargest(nums1,k)
		elif k > len(nums)-len(nums2):
			return self.kthLargest(nums2, k-(len(nums)-len(nums2)))
		
		return pivot



element = LargestElement()
nums = [3,2,1,5,6,4]
print(element.kthLargest(nums,2))
