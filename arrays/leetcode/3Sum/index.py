"""
:Author: Pravallika
:Description: Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
:Note: The solution set must not contain duplicate triplets
:Explanation: For example, given array S = [-1, 0, 1, 2, -1, -4],

		A solution set is:
		[
  		[-1, 0, 1],
  		[-1, -1, 2]
		]
"""

class ThreeSum(object):
	def threeSum(self,nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		
		result = []
		nums.sort()
		
		for i in range(len(nums)-1):
			if i>0 and nums[i] == nums[i-1]:
				continue
			l = len(nums)-1
			r = i+1
			
			while r<l:
				currSum = nums[i] + nums[r] + nums[l]
				if currSum < 0:
					r = r+1
				elif currSum > 0:
					l = l-1
				else:
					result.append([nums[i], nums[r], nums[l]])	
					while r<l and nums[r] == nums[r+1]:
						r = r+1
					while r<l and nums[l] == nums[l-1]:
						l = l-1
					r = r+1
					l = l+1
		return result


threeSum = ThreeSum()
nums = [-2,0,0,2,2]
print(threeSum.threeSum(nums))
