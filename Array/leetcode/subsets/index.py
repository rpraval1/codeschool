"""
:Author: Pravallika
:Description: Given a set of distinct integers, nums, return all possible subsets.
:Explanation: For example,
		If nums = [1,2,3], a solution is:

		[
			[3],
			[1],
			[2],
			[1,2,3],
			[1,3],
			[2,3],
			[1,2],
			[]
		]
"""

class Subsets(object):
	def subsets(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		
		result = [[]]
		nums.sort()
		
		for i in range(len(nums)):
			size = len(result)
			for j in range(size):
				result.append(list(result[j]))
				result[-1].append(nums[i])

		return result


sub = Subsets()
nums = [1,2,3]

print(sub.subsets(nums))
