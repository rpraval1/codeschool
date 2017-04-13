"""
:Author: Pravallika
:Description: Say you have an array for which the ith element is the price of a given stock on day i.

		If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
:Explanation: nput: [7, 1, 5, 3, 6, 4]
		Output: 5

		max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
"""

class Stocks(object):
	def sellStocks(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		min = nums[0]
		max = 0
		
		for cost in nums:
			if cost < min:
				min = cost
			if cost-min > max:
				max = cost-min

		return max


stock = Stocks()
nums = [7,1,5,3,6,4]
print(stock.sellStocks(nums))
