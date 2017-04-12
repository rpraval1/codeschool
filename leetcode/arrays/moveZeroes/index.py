"""
:Author: Pravallika
:Description: Given an array nums, move all 0's to end while maintaining the relative order of non-zero elements
:Explanation: nums = [0,1,0,3,12] resulting nums = [1,3,12,0,0]
"""

class MoveZeroes(object):
	def moveZeroes(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		for i in nums:
			if i == 0:
				nums.remove(0)
				nums.append(0)
		return nums

moveZeroes = MoveZeroes()
nums = [0,1,0,3,12]
print(moveZeroes.moveZeroes(nums))
