"""
:Author: Pravallika
:Description: Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.
:Note: The length of both num1 and num2 is < 110.
	Both num1 and num2 contains only digits 0-9.
	Both num1 and num2 does not contain any leading zero.
	You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

class StringMultiply(object):
	def multiply(self, nums1, nums2):
		"""
		:type nums1: str
		:type nums2: str
		:rtype: str
		"""
		
		nums1 = nums1[::-1]
		nums2 = nums2[::-1]
		
		m = len(nums1)
		n = len(nums2)
		
		result = [0]*(m+n)
		
		for i in range(m):
			for j in range(n):
				result[i+j] += (int(nums1[i])*int(nums2[j]))
				result[i+j+1] += result[i+j]//10
				result[i+j] %= 10
		
		k = len(result)-1
		while k>0 and result[k]==0:
			k = k-1
		
		return ''.join(map(str, result[k::-1]))


strMul = StringMultiply()
nums1 = "21"
nums2 = "10"

print(strMul.multiply(nums1,nums2))
