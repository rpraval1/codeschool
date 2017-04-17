"""
:Author: Pravallika
:Description: Implement pow(x, n).

"""

class Pow(object):

	def findPow(self, x, n):
		"""
		:type x: float
		:type n : int
		:rtype: float
		"""
		
		result = 1
		
		abs_n = abs(n)
		
		while abs_n:
			if abs_n & 1:
				result *= x
			abs_n >>= 1
			x *= x
			
		return 1/result if n<0 else result



obj = Pow()

print(obj.findPow(2,4))
