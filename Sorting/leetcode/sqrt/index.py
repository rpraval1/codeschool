"""
:Author: Pravallika
:Description: Implement int sqrt(int x).

		Compute and return the square root of x.
"""

class Sqrt(object):
	
	def findSqrt(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		
		if x < 1:
			return 0

		if x < 4:
			return 1

		
		right = x//2
		left = 2

		while left <= right:
			mid = (left + right)//2

			if mid*mid == x:
				return mid
			
			if left == mid:
				return left

			if mid*mid > x:
				right = mid
			elif mid*mid < x:
				left = mid


obj = Sqrt()
print(obj.findSqrt(16))
			
			
