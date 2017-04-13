"""
:Author: Pravallika
:Description: Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
:Explanation: Given [100, 4, 200, 1, 3, 2],
		The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

		Your algorithm should run in O(n) complexity.
"""
class LongestConsecutive(object):
	def longestConsecutive(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		result = 0
		numSet = set()
		
		for num in nums:
			numSet.add(num)

		for i in range(len(nums)):
			if(nums[i]-1 not in numSet):
				j = nums[i]
				while (j in numSet):
					j = j+1
				result = max(result,j-nums[i])
		return result


nums = [100,4,200,1,3,2]

lonConSeq = LongestConsecutive()
print(lonConSeq.longestConsecutive(nums))
