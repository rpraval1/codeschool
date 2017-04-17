"""
:Author: Pravallika
:Description: Given a list of non-negative numbers and a target integer k, 

		write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k, 

		that is, sums up to n*k where n is also an integer. 

:Explanation: Example 1:

		Input: [23, 2, 4, 6, 7],  k=6
		
		Output: True
		
		Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.

		Example 2:

		Input: [23, 2, 6, 4, 7],  k=6

		Output: True
		
		Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
"""

class MaxSubArr(object):

	def isSumMultiple(self, nums, k):
	
		"""
		:type nums: List[int]
		:type k: int
		:rtype: bool

		"""
		
		count = 0
		lookup = {0: -1}

		for i,num in enumerate(nums):
			count += num
			if k:
				count %= k
			if count in lookup:
				if i-lookup[count] > 1:
					return True

			else:
				lookup[count] = i


		return False


obj = MaxSubArr()
nums= [23,2,4,6,7]

print(obj.isSumMultiple(nums, 6))		
		
