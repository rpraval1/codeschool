"""
:Author: Pravallika
:Description: You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.
:Explanation: Input: nums is [1, 1, 1, 1, 1], S is 3. 
		Output: 5
		Explanation: 

		-1+1+1+1+1 = 3
		+1-1+1+1+1 = 3
		+1+1-1+1+1 = 3
		+1+1+1-1+1 = 3
		+1+1+1+1-1 = 3

		There are 5 ways to assign symbols to make the sum of nums be target 3.
"""
import collections
class TargetSum(object):
	def targetSum(self,nums,S):
		"""
		:type nums: List[int]
		:type S: int
		:rtype: int
		"""
		def subsetSum(nums,S):
			dp = collections.defaultdict(int)
			dp[0] = 1
			
			for n in nums:
				for i in reversed(range(n,S+1)):
					if i-n in dp:
						dp[i] = dp[i] + dp[i-n]
			return dp[S]


		total = sum(nums)
		if total < S or (total+S)%2:
			return 0
		P = (S+total)//2
		return subsetSum(nums,P)


nums = [1,1,1,1,1]
print(TargetSum().targetSum(nums,3))
