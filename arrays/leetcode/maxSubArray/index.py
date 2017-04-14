"""
:Author: Pravallika
:Description: Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.
:Example: nums = [1,-1,5,-2,3] , k=3 return 4, beacuse [1,-1,5,-2] sums to 3
"""

class MaxSubArray(object):
	def maxSubArray(self,nums,k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: int
		"""
		sums = {}
		currSum = 0
		maxLen = 0
		
		for i in range(len(nums)):
			currSum = currSum + nums[i]
			if currSum == k:
				maxLen = i + 1
			elif currSum-k in sums:
				maxLen = max(maxLen, i-sums[currSum-k])
			if currSum not in sums:
				sums[currSum] = i
		return maxLen


subArr = MaxSubArray()
nums = [1,-1,5,-2,3]
k = 3
print(subArr.maxSubArray(nums,k))
