
"""
:Author: Pravallika
:Description: Given a collection of integers that might contain duplicates, nums, return all possible subsets.
:Note: The solution set must not contain duplicate subsets.
:Explanation: For example,
		If nums = [1,2,2], a solution is:

		[
  			[2],
  			[1],
  			[1,2,2],
  			[2,2],
  			[1,2],
  			[]
		]

"""


class Subset(object):
	def findSubsets(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		
		res = [[]]
		
		nums.sort()
		for i in range(len(nums)):
			if i == 0 or nums[i] != nums[i-1]:
				l = len(res)
			for j in range(len(res)-l,len(res)):
				res.append(res[j] + [nums[i]])
		
		return res


obj = Subset()

nums= [1,2,2]
print(obj.findSubsets(nums))
