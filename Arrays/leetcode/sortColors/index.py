"""
:Author: Pravallika
:Description: Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

		Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
:Explanation: For example nums = [0,2,1,0,1,2]
			resulted nums = [0,0,1,1,2,2]

"""

class SortedColors(object):
	def sort(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		
		start = 0
		end = len(nums)-1
		
		i = 0
		
		while(i<=end):
			if nums[i] == 2:
				nums[i], nums[end] = nums[end], nums[i]
				end = end-1
			elif nums[i] == 0:
				nums[i], nums[start] = nums[start], nums[i]
				start = start + 1
				i = i+1
			else:
				i = i+1
		print(nums)


sort = SortedColors()

nums = [0,2,1,0,1,2]
sort.sort(nums)	 
