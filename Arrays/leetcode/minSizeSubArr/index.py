"""
:Author: Pravallika
:Description: Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. 
		If there isn't one, return 0 instead.
:Explanation: For example, given the array [2,3,1,2,4,3] and s = 7,
		the subarray [4,3] has the minimal length under the problem constraint.
"""

class SubArray(object):
	def minSize(self, s, nums):
		"""
		:type s: int
		:type nums: List[int]
		"""
		
		currSum = 0
		start = 0
		minSize = float("inf")
		
		for i in range(len(nums)):
			currSum += nums[i]
			while currSum >= s:
				minSize = min(minSize, i-start+1)
				currSum -= nums[start]
				start += 1

		if minSize != float("inf"):
			return minSize
		else:
			return 0




subarr = SubArray()
nums = [2,3,1,2,4,3]
print(subarr.minSize(7,nums))
