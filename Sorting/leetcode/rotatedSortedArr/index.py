"""
:Author: Pravallika
:Description: Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

	(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

	You are given a target value to search. If found in the array return its index, otherwise return -1.

	You may assume no duplicate exists in the array.
"""

class RotateSortArr(object):
	def findTarget(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		
		left = 0
		right = len(nums)-1
		
		while left<=right:
			mid = left + (right-left)//2
			
			if target == nums[mid]:
				return mid
			
			if (nums[mid]>=nums[left] and nums[left]<=target<nums[mid]) or (nums[mid]<nums[left] and not (nums[mid]<target<=nums[right])):
				right = mid-1
			else:
				left = mid+1
		return -1



obj = RotateSortArr()
nums = [4,5,6,7,0,1,2]
print(obj.findTarget(nums,5)) 
