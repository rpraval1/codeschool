"""
:Author: Pravallika
:Description: Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

		Solve it without division and in O(n).
:Explanation: 
		For example, given [1,2,3,4], return [24,12,8,6].
"""

class ArrayProduct(object):
	def productItself(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		
		p = 1
		
		output = []
		
		n = len(nums)
		for i in range(n):
			output.append(p)
			p = p * nums[i]

		p = 1
		for i in range(n-1,-1,-1):
			output[i] = output[i]*p
			p = p * nums[i]

		return output



sol = ArrayProduct()
nums = [1,2,3,4]
print(sol.productItself(nums))
