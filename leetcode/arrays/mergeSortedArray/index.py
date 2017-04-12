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
		result = []
		while i<m and j<n:
			print(i,j)
			if nums1[i] > nums2[j]:
				result.append(nums2[j])
				j = j+1
			else:
				result.append(nums1[i])
				i = i+1
		  	if i == m:
				result.append(nums1[i])
			elif j == n:
				result.append(nums2[j])
				 
		print(result)


merge = MergeSorted()
nums1 = [2,3,5,7]
m = 4
nums2 = [1,4,6,8]
n = 4
merge.mergeSortedArray(nums1,m,nums2,n)
