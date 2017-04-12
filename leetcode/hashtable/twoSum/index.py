"""
:Author: Pravallika
:Description: Given an array of integers, return indices of the two numbers such that they add up to a specific target.
:Example: nums=[2, 7, 11. 15] target = 9  return [0,1]
:Explanation: nums[0]+nums[1] = 2+7 = 9
"""

class TwoSum(object):
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		lookup = {}
		for i,num in enumerate(nums):
			if target-num in lookup:
				return [lookup[target-num],i]
			lookup[num] = i

		return []


sum = TwoSum()
nums = [2, 7, 11, 15]
target = 9
print(sum.twoSum(nums,target))
