"""
:Author: Pravallika
:Description: Given two sorted integer arrays num1 and num2, merge nums2 into nums1 as one sorted array.
:Example: nums1 = [2,4,6,7,9] nums2 = [1,3,6,8] resulted nums1 = [1,2,3,4,6,6,7,8,9]
"""
class MergeSorted(object):
	def mergeSortedArray(self, nums1, m, nums2, n):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:type m: int
		:type n: int
		:rtype: void
		"""
		i = 0 
		j = 0

		while i<m and j<n:
			print(i,j)
			if nums1[i] > nums2[j]:
				
				nums1.append(nums2[j])
				if j == n-1 and i == m-1:
					nums1.append(nums1[i])
				j = j+1
			else:
				nums1.append(nums1[i])
				if i == m-1 and j == n-1:
					nums1.append(nums2[j])
				i = i+1

		for i in range(m):
			nums1.pop(0)
		
		print(nums1)	


merge = MergeSorted()
nums1 = [2,3,5,7]
m = 4
nums2 = [1,4,6,8]
n = 4
merge.mergeSortedArray(nums1,m,nums2,n)
